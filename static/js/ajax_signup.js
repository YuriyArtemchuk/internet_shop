$(document).ready(() => {
    console.log('signup.js -> OK');

    // Global:
    // =====================================================================
    console.log('script -> start');
    let loginIsValid = false;
    let pass1IsValid = false;
    let pass2IsValid = false;
    let emailIsValid = false;
    // =====================================================================

    // Login:
    // =========================================================================
    const loginInput = $('#login');
    loginInput.blur(() => {
        console.log('login -> blur');
        let login = loginInput.val();
        console.log('login -> ' + login);
        let pattern = /^[a-zA-Z][a-zA-Z0-9_\-\.]{5,15}$/;
        let message = 'Логін довжиною від 6 до 16 символів, перший - буква, ';
        message += ' інші - букви (великі або маленькі), цифри, _, -, .';
        // Перевірка валідності логіна
        // ===========================
        if (pattern.test(login)) {
            // Перевірка занятості логіну:
            // ===========================
            console.log('pattern -> ok');
            $.ajax({
                url: '/account/ajax_signup',
                data: `login=${login}`,
                success: function(response) {
                    console.log('ajax -> signup');
                    console.log('message -> ', response.message_login);
                    // console.log('user_name1 -> ', response.user_name1);
                    // console.log('user_name2 -> ', response.user_name2);
                    // console.log('ajax_message 1->', response.ajax_message1);
                    // console.log('ajax_message 3->', response.ajax_message3);
                    console.log('ajax_message ->', response.ajax_message)
                    console.log('quntity ->', response.quntity)
                    //
                    let result = response.ajax_message
                    if (result === 'Ok') {
                        console.log('result = Ok')
                        $('#login-err').text('Логін зайнятий');
                        loginInput.css('box-shadow', '0 0 10px red');
                        loginIsValid = false;
                    } else {
                        console.log('result = not Ok')
                        loginInput.css('box-shadow', '0 0 10px green');
                        $('#login-err').text('');
                        // Якщо логіна немає в базі даних, то success нічого не повертає і не діє $('#login-err').text('Логін не зайнятий');
                        loginIsValid = true;
                    }
                }
            });
        } else {
            console.log('pattern -> not ok');
            loginInput.css('box-shadow', '0 0 10px red');
            $('#login-err').text(message);
            loginIsValid = false;
        }
    
    });

    // Pass1:
    // =========================================================================
    const pass1Input = $('#pass1');
    pass1Input.blur(() => {
        console.log('pass1 -> blur');
        let pass1 = pass1Input.val();
        let pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9_\-\.]{8,}$/;
        let message = 'Пароль довжиною від 8, хоча б одна велика літера, ';
        message += 'хоча б одна маленька літера, хоча б одна цифра, ';
        message += 'інші - букви (великі або маленькі), цифри, _, -, .';
        //
        if (pattern.test(pass1)) {
            $('#pass1-err').text('');
            pass1Input.css('box-shadow', '0 0 10px green');
            pass1IsValid = true;
        } else {
            $('#pass1-err').text(message);
            pass1Input.css('box-shadow', '0 0 10px red');
            pass1IsValid = false;
        }
    });

    // Pass2:
    // =========================================================================
    const pass2Input = $('#pass2');
    pass2Input.blur(() => {
        console.log('pass2 -> blur');
        let pass1 = pass1Input.val();
        let pass2 = pass2Input.val();
        let message = "Введені паролі не співпадають";
        //
        if (pass1 === pass2) {
            $('#pass2-err').text('');
            pass2Input.css('box-shadow', '0 0 10px green');
            pass2IsValid = true;
        } else {
            $('#pass2-err').text(message);
            pass2Input.css('box-shadow', '0 0 10px red');
            pass2IsValid = false;
        }
    });

    // Email:
    // =========================================================================
    const emailInput = $('#email');
    emailInput.blur(() => {
        console.log('email -> blur');
        let email = emailInput.val();
        let pattern = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;
        let message = 'Не корректно введний Email!';
        // Перевірка валідності email
        console.log('email -> after blur')
        // ===========================
        if (pattern.test(email)) {
            // Перевірка занятості email:
            // ===========================
            console.log('email -> before ajax');
            $.ajax({
                url: '/account/ajax_email',
                data: `email=${email}`,
                success: function(response) {
                    console.log('message_email ->', response.message_email)
                    console.log('ajax_email ->', response.ajax_email)
                    console.log('quantity ->', response.quantity)
                    let result = response.ajax_email;
                    if (result === 'not Ok') {
                        emailInput.css('box-shadow', '0 0 10px green');
                        $('#email-err').text('');
                        emailIsValid = true;
                    } else {
                        emailInput.css('box-shadow', '0 0 10px red');
                        $('#email-err').text('Email зайнятий');
                        emailIsValid = false;
                    }
                }
            });
        } else {
            console.log('email -> after pattern')
            emailInput.css('box-shadow', '0 0 10px red');
            $('#email-err').text(message);
            emailIsValid = false;
        }
    });

    // Submit - приклад синтаксису jquery:
    // =========================================================================
    $('#submit').click((event) => {
        console.log('submit -> click');
        console.log(loginIsValid);
        console.log(pass1IsValid);
        console.log(pass2IsValid);
        console.log(emailIsValid);
        if (loginIsValid && pass1IsValid && pass2IsValid && emailIsValid) {
            console.log("Ok");
        } else {
            console.log('not ok');
            event.preventDefault();
            alert("Відправка даних заблокована валідатором!");
        }
    });

    });


