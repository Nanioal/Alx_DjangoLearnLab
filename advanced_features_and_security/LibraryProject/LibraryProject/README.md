# Django Application Security Measures

## Secure Settings
- **DEBUG**: Set to `False` in production.
- **SECURE_BROWSER_XSS_FILTER**: Enabled to prevent XSS attacks.
- **X_FRAME_OPTIONS**: Set to `DENY` to prevent clickjacking.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Enabled to prevent MIME type sniffing.
- **CSRF_COOKIE_SECURE**: Ensures CSRF cookies are sent over HTTPS.
- **SESSION_COOKIE_SECURE**: Ensures session cookies are sent over HTTPS.

## CSRF Protection
- Added `{% csrf_token %}` in all form templates to protect against CSRF attacks.

## Secure Data Access in Views
- Used Django's ORM to avoid SQL injection.
- Validated and sanitized user inputs using Django forms.

## Content Security Policy (CSP)
- Configured CSP headers using django-csp middleware to reduce the risk of XSS attacks.

## Testing
- Manually tested the application to check for secure handling of inputs and responses.
- Verified CSRF and XSS protections by attempting various attacks and ensuring they are blocked.
