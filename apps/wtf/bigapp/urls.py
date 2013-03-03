from bigapp import app
import views

app.add_url_rule('/', 'home', views.home)
app.add_url_rule('/employees', 'employee', views.employee_list)
app.add_url_rule('/employees/add', 'employee_add', views.employee_add, methods=['GET', 'POST'])
app.add_url_rule('/employees/update/<int:id>', 'employee_update', views.employee_update, methods=['GET', 'POST'])
