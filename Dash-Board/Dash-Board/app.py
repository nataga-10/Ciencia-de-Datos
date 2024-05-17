from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static')


# Función para servir imágenes estáticas desde la carpeta 'templates'
@app.route('/templates/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates'), filename)

@app.route('/show_images')
def show_images():
    # Rutas de las imágenes generadas
    images = [
        'top_cves_por_fecha.png',
        'cve-criticidad.png',
        'cve-maquinas.png',
        'cves.png',
        'top_cves_criticidad.png',
        'heatmap_cves.png',       
    ]
    # Lista para almacenar las rutas completas de las imágenes
    image_paths = []

    for image in images:
        image_paths.append(image)

    return render_template('dashboard.html', image_paths=image_paths)

if __name__ == "__main__":
    app.run(debug=True)