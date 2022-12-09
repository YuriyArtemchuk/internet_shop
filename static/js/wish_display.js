$(document).ready(() => {
    console.log('wish_display.js -> OK');
    const userId = $('#user_id').val();
    console.log('User-ID: ' + userId);

    if (userId != "None") {
    // Відправка AJAX запиту на сервер для виводу <Обраних> товарів на всі сторінки сайту
        $.ajax({
        url: '/wish/ajax_wish_display',
        data: `uid=${userId}`,
        success: (response) => {
            console.log('AJAX_wish_display -> work');
           //
           $('#wish-count').text(" " + response.count);
           $('.wish-summary').find('h5').text(response.count + ' товарів вибрано');
           $('.wish-summary').find('h4').text('Вартість: ' + response.amount_wish + ' грн');
           }
       });
       }

});