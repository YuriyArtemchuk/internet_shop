$(document).ready(() => {

    console.log('delivery.js -> OK');

    $('#f-option7').click((event) => {
        console.log('delivery -> Start');
        // 
        let order = $('#order').val();
        console.log("order->" + order)
        //         
        const first = $('#first').val();
        console.log("first ->" + first)
        // 
        const last = $('#last').val();
        console.log("last ->" + last)
        // 
        const phone = $('#phone').val();
        console.log("phone ->" + phone)
        // 
        const company = $('#company option:selected').text();
        console.log('company ->' + company);
        // 
        const city = $('#city').val();
        console.log("city ->" + city)
        // 
        const depot = $('#depot').val();
        console.log("depot ->" + depot)
        // 
        const info = $('#info').val();
        console.log("info ->" + info)
        // 
        const init = $('#init').val();
        console.log('init - >' + init)

        // 
            $.ajax({
                url: '/orders/ajax_delivery_info',
                data: `first=${first}&last=${last}&phone=${phone}&company=${company}&city=${city}&order=${order}&init=${init}`,
                // data: `first=${first}&last=${last}&test=${test}&phone=${phone}&company=${company}&city=${city}&depot=${depot}&address=${address}&info=${info}`,
                success: (response) => {
                    console.log("ajax_delivery -> Ok");
                    console.log("ajax order ->" + response.order);
                    console.log("ajax init ->" + response.init);
                    console.log('ajax first ->' + response.first);
                    console.log('ajax last ->' + response.last);
                    console.log('ajax phone ->' + response.phone);
                    console.log('ajax company ->' + response.company);
                    console.log('ajax city ->' + response.city);
                    // console.log('ajax depot ->' + response.depot);
                    // console.log('ajax address ->' + response.address);
                    // console.log('ajax info ->' + response.info);
                    // 
                    console.log('delivery_id ->' + response.delivery_id)
                    $('#my-order').val(response.delivery_id);
                    // 
                    if (response['result'] === 'Ok') {
                        console.log('Ok');
                        let initList = response.init;
                        console.log("initList", initList)
                        let orderId = response.order;
                        console.log("orderId", orderId)
                        $('#result').html('');
                        var insert_result = `<p><a href="/orders/confirm/${initList}/${orderId}" class="btn primary-btn bill-btn my-order" type="submit" role="button">Підтвердження замовлення</a></p>`;
                        $('#result').html(insert_result);

                    } 
                    
                    
                    // else {
                    //     console.log('not Ok');
                    //     event.preventDefault();
                    //     alert("Не всі дані заповнені");
                    // }
                }
            });
       
    });

});