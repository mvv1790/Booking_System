function validateForm() {
    var name = document.forms['formSection']['name'].value;
    var email = document.forms['formSection']['email'].value;
    if (name == "") {
        alert('Name must be filled out');
        return false;
    }
    if (email == "") {
        alert('Email must be filled out')
        return false;
    }
    return true;
}