from django.contrib import admin


class CustomAdminSite(admin.AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = "Admin"

    # Text to put in each page's <h1>.
    site_header = "Admin"

    # Text to put at the top of the admin index page.
    index_title = "Admin"
