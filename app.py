from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app = Flask(__name__)

# initialize scheduler
scheduler = BackgroundScheduler()

@app.route('/generate', methods=['GET'])
def generate_blog_post():
    """
    Endpoint to generate a blog post for a given keyword.
    Query parameter: keyword (str) - The topic to generate a blog post about
    Returns: JSON response with the generated blog post
    """
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({'error': 'Keyword parameter is required'}), 400
    
    # TODO: Implement blog post generation logic
    # 1. Get SEO metrics using seo_fetcher
    # 2. Generate blog post using ai_generator
    # 3. Return the generated content
    
    return jsonify({
        'status': 'success',
        'keyword': keyword,
        'generated_at': datetime.now().isoformat(),
        'content': 'Blog post content will be generated here'
    })

def scheduled_blog_generation():
    """
    Function to be called by the scheduler for daily blog post generation.
    Uses a predefined keyword to generate a new blog post.
    """
    # TODO: Implement daily blog generation logic
    # 1. Use a predefined keyword
    # 2. Call the generate_blog_post function
    # 3. Save the generated content to a file
    pass

if __name__ == '__main__':
    # start the scheduler
    scheduler.add_job(scheduled_blog_generation, 'interval', days=1)
    scheduler.start()
    
    # run the Flask app
    app.run(debug=True) 