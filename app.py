import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from utils.document_verifier import verify_document
from utils.social_media import get_social_media_data
from utils.esports_validator import validate_esports_profile

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config.from_pyfile('config.py')

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Save basic info to session
        session['user_data'] = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'cpf': request.form.get('cpf'),
            'address': request.form.get('address'),
            'birth_date': request.form.get('birth_date'),
            'interests': request.form.get('interests'),
            'favorite_teams': request.form.get('favorite_teams'),
            'events_attended': request.form.get('events_attended'),
            'merch_purchased': request.form.get('merch_purchased')
        }
        return redirect(url_for('documents'))
    return render_template('profile.html')

@app.route('/documents', methods=['GET', 'POST'])
def documents():
    if 'user_data' not in session:
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        if 'document' not in request.files:
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        file = request.files['document']
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Verify document with AI
            verification_result = verify_document(filepath, session['user_data']['cpf'])
            session['document_verified'] = verification_result['verified']
            session['document_path'] = filepath
            
            if verification_result['verified']:
                flash('Documento verificado com sucesso!')
                return redirect(url_for('social'))
            else:
                flash('Falha na verificação do documento. Por favor, tente novamente.')
    
    return render_template('documents.html')

@app.route('/social', methods=['GET', 'POST'])
def social():
    if 'user_data' not in session or 'document_verified' not in session:
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        social_data = {
            'twitter': request.form.get('twitter'),
            'facebook': request.form.get('facebook'),
            'instagram': request.form.get('instagram'),
            'twitch': request.form.get('twitch')
        }
        
        # Get social media data
        session['social_data'] = get_social_media_data(social_data)
        return redirect(url_for('esports'))
    
    return render_template('social.html')

@app.route('/esports', methods=['GET', 'POST'])
def esports():
    if 'user_data' not in session or 'social_data' not in session:
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        esports_profiles = {
            'furia': request.form.get('furia_profile'),
            'faceit': request.form.get('faceit_profile'),
            'steam': request.form.get('steam_profile'),
            'other': request.form.get('other_profiles')
        }
        
        # Validate esports profiles
        validation_results = {}
        for platform, url in esports_profiles.items():
            if url:
                validation_results[platform] = validate_esports_profile(url, session['user_data']['email'])
        
        session['esports_profiles'] = validation_results
        return redirect(url_for('summary'))
    
    return render_template('esports.html')

@app.route('/summary')
def summary():
    if 'user_data' not in session:
        return redirect(url_for('profile'))
    
    user_data = session.get('user_data', {})
    document_verified = session.get('document_verified', False)
    social_data = session.get('social_data', {})
    esports_profiles = session.get('esports_profiles', {})
    
    return render_template('summary.html',
                         user_data=user_data,
                         document_verified=document_verified,
                         social_data=social_data,
                         esports_profiles=esports_profiles)

if __name__ == '__main__':
    app.run(debug=True)