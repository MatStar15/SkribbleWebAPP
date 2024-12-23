from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from db import get_db

def add_routes(app):


    @app.route('/')
    def hello_world():  # put application's code here
        return render_template('index.html')

    @app.route('/save', methods=['POST'])
    def save_image():
        try:
            # Get the canvas data
            canvas_data = request.form.get("canvas_data")
            print("[INFO] Received an Image successfully")

            # Save the image to the server
            db = get_db()

            db.execute("INSERT INTO image_gallery (data) VALUES (?)",
                       (canvas_data,) )
            # (canvas_data,) is a tuple with one element so that it can be passed as a parameter to the execute function without any issues
            db.commit()

            return jsonify({"message": "Image saved successfully"}), 201

        except Exception as e:  # Catch any errors during processing
            print(f"Error saving image: {e}")
            return jsonify({"error": str(e)}), 500  # Indicate server error


    @app.route('/gallery')
    def gallery():
        db = get_db()
        images = db.execute("SELECT * FROM image_gallery").fetchall()
        return render_template('gallery.html', images=images)  # Pass the images to the gallery.html template
