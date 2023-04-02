const calculate = () => {
    // 1
    let checkedCells = $('.check:checked');
    let totalPrice = 0;
    let selItemsList = '';

    // 2
    for (let cell of checkedCells) {
        let parentRow = $(cell).parent().parent();
        totalPrice += parseFloat($(parentRow).find('td.total_price_cell').text());
        selItemsList += $(parentRow).find('td.id_cell').text() + ',';
//        console.log(selItemsList)
    }
    selItemsList += totalPrice;

    // 3
    console.log(`totalPrice = ${totalPrice}`);
    console.log(`selItemsList = ${selItemsList}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн.`);
    $('.bill-btn').attr('href', `/orders/order/${selItemsList}`);
   
};

$(document).ready(() => {
    console.log('calc_cart -> work');
    calculate();

    $('.check').click(() => {
        console.log('check -> CLick')
        calculate();
    });

});

$(document).ready(function() {
    console.log('qty')
    $(document).on("change", ".qty-product", function() {
        let current_quantity = parseInt($(this).val());
        console.log("type1", typeof(current_quantity))
        if (current_quantity >= 1) {
            // console.log('instanceof', (current_quantity instanceof Number))
            console.log("current_quantity", current_quantity);
            let current_tr = $(this).closest('tr');
            let current_price = parseFloat(current_tr.find(".product_price").text()).toFixed(2);
            console.log(current_price, typeof(current_price));
            let new_product_amount = parseFloat(current_price * current_quantity).toFixed(2);
            console.log(new_product_amount, typeof(new_product_amount));
            let user_id = $('#user_id').val();
            let prod_id = current_tr.find('.id_cell').text();
            //
            current_tr.find(".total_price_cell").text(new_product_amount); 
            calculate();
            //
            info_data = {};
            info_data.prod_id = prod_id;
            info_data.current_qty = current_quantity;
            $.ajax({
                url: "/cart/ajax_change_qty",
                data: info_data,
                success: function(response) {
                    console.log("ajax_gty => Start");
                    console.log('changed_qty', response.changed_qty);   
                },
            })
        } else {
            alert("Кількість товарів не може бути меньшою за 1")
            current_quantity ++
            $(this).val(current_quantity)
            
        }
    })
    
})