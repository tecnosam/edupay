
function payWithPaystack(service, email){
    var handler = PaystackPop.setup({
        key: 'pk_test_631c0885f9a110b544cf365840fbb474d90314f4',
        email: email,
        amount: service.amount*100,  // must be in KOBO
        metadata: {
            custom_fields: [
                {
                    display_name: "Service Name",
                    variable_name: "service_name",
                    value: service.name
                },
                {
                    display_name: "Service Price",
                    variable_name: "amount_paid",
                    value: service.amount
                },
            ]
        },
        callback: function(response){
            // alert('success. transaction ref is ' + response.reference);
            window.location.pathname = `/services/${service.id}/place-order/${response.reference}`;
        },
        onClose: function(){
            // alert('window closed');
        }
    });
    handler.openIframe();
}