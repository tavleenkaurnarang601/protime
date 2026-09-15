# Database

Django migrations define `Company`, custom `User`, `Project`, `Task`, and `AuditLog`. The custom User model adds company and role (Admin, Manager, Employee) while retaining Django's secure password storage. `Project` names are unique within a company.

Apply changes with `py manage.py migrate`.