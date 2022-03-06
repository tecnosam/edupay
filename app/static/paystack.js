
function payWithPaystack(amount=100, product_id=1, email='ikabolo59@gmail.com'){
    var handler = PaystackPop.setup({
        key: 'pk_test_631c0885f9a110b544cf365840fbb474d90314f4',
        email: email, // TODO: change to users email
        amount: amount*100,  // must be in KOBO
        metadata: {
            // custom_fields: [
            //     {
            //         display_name: "Mobile Number",
            //         variable_name: "mobile_number",
            //         value: "+2348012345678"
            //     }
            // ]
        },
        callback: function(response){
            // TODO: forward response to Database
            alert('success. transaction ref is ' + response.reference);
        },
        onClose: function(){
            // alert('window closed');
        }
    });
    handler.openIframe();
}