$(document).ready(() => {
    console.log('wish.js -> OK');

   $('.products').on('click', '.add-to-wish', (event) => {
        console.log(event.target)
        console.log('wish-btn -> OK');
        //
        const userId = $('#user_id').val();
        console.log('User-ID -> ' + userId);
        //
        if (userId == "None") {
            alert('Для збереження <ОБРАНИХ> товарів у базі даних Ви повинні авторізуватись!')
        }
        else {
            let wishId = $(event.target).parent().prev().val();
            console.log('wishId ->' + wishId);
           // Відправка AJAX запиту на сервер для збереження товарів з <Обраних> в базі даних
            $.ajax({
                url: '/wish/ajax_wish',
                data: `uid=${userId}&pid=${wishId}`,
                success: (response) => {
                    console.log('AJAX_wish -> work');
                    console.log('UID: ' + response.uid);
                    console.log('PID: ' + response.pid);
                    //
                    $('#wish-count').text(response.count);
                    $('.wish-summary').find('h5').text(response.count + ' товарів вибрано');
                    $('.wish-summary').find('h4').text('Вартість: ' + response.amount_wish + ' грн');
               }
            });
        }
    });
});