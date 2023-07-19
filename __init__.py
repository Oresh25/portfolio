from flask import Flask, render_template,abort

def create_app():
    app = Flask(__name__)

    projects = [
        {
            "name": "REST API",
            "thumb": "img/REST1.jpg",
            "hero": "img/REST-hero.jpg",
            "categories": ["python", "Flask", "Docker"],
            "slug": "REST-API",
            "prod": "https://github.com/Oresh25/REST_API"
        },
        {
            "name": "MicroBlog app",
            "thumb": "img/microblog.JPG",
            "hero": "img/microblog-hero.jpeg",
            "categories": ["python", "Flask", "html", "css", "MongoDB"],
            "slug": "MicroBlog",
            "prod": "https://github.com/Oresh25/Web-MicroBlog"
        },
        {
            "name": "Cocktail web",
            "thumb": "img/cocktail.jpg",
            "hero": "img/cocktail_about.jpg",
            "categories": ["html", "css", "JAVASCRIPT", "PHP"],
            "slug": "Cocktail_web",
            "prod": "https://github.com/Oresh25/Web-Project"
        }
    ]

    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)


    @app.route("/about")
    def about():
        return render_template("about.html")


    @app.route("/contact")
    def contact():
        return render_template("contact.html")


    @app.route("/projects/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(
            f"project_{slug}.html", 
            project = slug_to_project[slug]
        )


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404
    
    return app