# Application endpoints

- `/` — protected role-aware dashboard
- `/login/`, `/register/`, `/logout/` — session authentication
- `/password-reset/` — Django password-reset request flow
- `/admin/` — Django administrator interface

CSRF protection is enforced for all state-changing HTML forms. JSON REST APIs will be introduced only when later milestones require a desktop agent or integration.