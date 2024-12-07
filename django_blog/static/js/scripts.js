document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
    
    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            const inputs = form.querySelectorAll('input');
            let isValid = true;
            
            inputs.forEach(function(input) {
                if (input.type !== 'submit' && input.value.trim() === '') {
                    isValid = false;
                    input.style.borderColor = 'red';
                } else {
                    input.style.borderColor = '';
                }
            });
            
            if (!isValid) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    });
    
    // Dynamic behavior (example: toggle password visibility)
    const togglePasswordVisibility = document.querySelector('.toggle-password');
    if (togglePasswordVisibility) {
        togglePasswordVisibility.addEventListener('click', function() {
            const passwordInput = document.querySelector('#password');
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                togglePasswordVisibility.textContent = 'Hide';
            } else {
                passwordInput.type = 'password';
                togglePasswordVisibility.textContent = 'Show';
            }
        });
    }
});
