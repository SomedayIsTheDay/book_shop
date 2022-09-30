window.onload = function () {
    $('.cart_list').on('click', 'input[type="number"]', (event) => {
        const target_href = event.target;
        $.ajax({
            url: "/cart/edit/" + target_href.name + "/" + target_href.value + "/",
            success: function (data) {
                $('.cart_list').html(data);
            },
        });
        event.preventDefault();
    });
}