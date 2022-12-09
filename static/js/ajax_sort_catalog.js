$(document).ready(() => {
    console.log('sort_catalog -> Start');

    // $('.my-category').on('click', '#choice-category', (event) => {

    $('.my-category').click((event) => {   
        console.log('choice-category -> Start');
        let categorySelect = $(event.target).val();  
        
        console.log('category ->' + categorySelect);
        $.ajax({
            url: '/catalog/ajax_sort_catalog',
            data: `category_name=${categorySelect}`,
            success:(response) => {
                console.log("ajax_sort ->" + response.category);
                console.log('ajax_category -> ' + response.current_category)
                // console.log('ajax_all_products -> ' + response.all_products)
                // $('.my-select').attr(`{% for product in ${paginate_products} %}`);         // як передати список в директиву

            }
        });

    });

});