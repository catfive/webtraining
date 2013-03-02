from bigapp import app
import views

app.add_url_rule('/', 'home', views.home)
app.add_url_rule('/employees', 'employee', views.employee_list)
