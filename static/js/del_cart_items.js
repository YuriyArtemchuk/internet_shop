$(document).ready(() => {
    console.log('del_cart_items -> work')

    $('.del-btn').click((event) => {
    let delId = $(event.target).prev().val();
    console.log(delId)
        $.ajax({
            url: '/cart/ajax_del_cart',
            data: `del_id=${delId}`,
            success: (response) => {
                alert(response.report);
                window.location = '/cart/index';
            }
        });

    });

});