
function payWithPaystack(product, email='ikabolo59@gmail.com'){
    var handler = PaystackPop.setup({
        key: 'pk_test_631c0885f9a110b544cf365840fbb474d90314f4',
        email: email, // TODO: change to users email
        amount: product.amount*100,  // must be in KOBO
        metadata: {
            custom_fields: [
                {
                    display_name: "Product Name",
                    variable_name: "product_name",
                    value: product.name
                },
            ]
        },
        callback: function(response){
            // alert('success. transaction ref is ' + response.reference);
            window.location.pathname = `/products/${product.id}/place-order/${response.reference}`;
        },
        onClose: function(){
            // alert('window closed');
        }
    });
    handler.openIframe();
}