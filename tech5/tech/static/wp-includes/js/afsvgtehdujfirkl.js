function ajaxObj(meth, url) {
    var x = new XMLHttpRequest();
    x.open(meth, url, true);
    x.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    return x;
}

function ajaxReturn(x) {
    if (x.readyState === 4 && x.status === 200) {
        return true;
    }
}

function ___(x) {
    return document.getElementById(x);
}

function __c(x) {
    return document.getElementsByClassName(x);
}

function restrict(elem) {
    var tf = ___(elem);
    var rx = new RegExp;
    if (tf.type === "email") {
        rx = /[^a-zA-Z0-9.@]/gi;
    } else if (tf.type === "text") {
        rx = /[^a-z0-9 ]/gi;
    }
    if (elem === "phone" || elem === "acct_num" || elem === "amount" || elem === "with_amount") {
        rx = /[^+,0-9. ()]/gi;
    }
    tf.value = tf.value.replace(rx, "");
}

function emptyElement(x) {
    ___(x).innerHTML = "";
}

function open_page() {
    var elem = ___('loader');
    elem.style.display = 'none';
}

function ShowPassform(x) {
    var elem = ___(x);
    if (elem.style.display == 'block') {
        elem.style.display = 'none';
        ___('sign-up').style.display = 'none';
        ___('sign-in').style.display = 'block';

    } else {
        elem.style.display = 'block';
        ___('sign-in').style.display = 'none';
        ___('sign-up').style.display = 'none';
    }
}

function ShowLogin() {
    window.location = "?sign-in";
}

function add_wallet() {
    var name = ___('wal_name').value;
    var add = ___('wallet_address').value;
    var btn = ___('add_wallet_btn');
    if ('' == name || '' == add) {
        return false;
    }
    btn.disabled = true;
    btn.textContent = 'processing...';
    var ajax = ajaxObj("POST", "index.php?add_w");
    ajax.onreadystatechange = function () {
        if (ajaxReturn(ajax) === true) {
            if (ajax.responseText === "success") {
                window.location = "?add-wallet";
            } else {
                alert(ajax.responseText);
                btn.disabled = false;
                btn.textContent = 'Add wallet';
            }
        }
    };
    ajax.send("w_name=" + name + "&w_add=" + add);
}

function add_data(x, y) {
    ___(y).value = x;
}

function add_data_class(x, y) {
    var min = ___('min_with').value;
    var max = ___('current_profit').value;
//    alert(min);
//    alert(max);
//    alert(x < max);
//    if(x < min){
//        alert('You can not go below minimum withdrawal!');
//        ___('amount').value = min;
//    }else if(x > max){
//        alert('You can not go above your available withdraw balance!');
//        ___('amount').value = max;
//    }
//    alert(x);
    $("#" + y).html('$' + x);
    $("#" + y + '1').html('$' + x);
    $("#" + y + '2').html('$' + x);
    var bal = ___('current_profit').value - x;
    if (bal < 1) {
        bal = 0;
    }
    $("#bal_amount").html('$' + bal);
}

function add_data_html(x, y) {
    ___(y).innerHTML = ___(x).value;
}

function remove_wallet(x) {
    var ask = confirm("Are you sure you want to remove account?");
    if (ask) {
        var btn = ___('wa_btn_' + x);
        btn.disabled = true;
        btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i>';
        var ajax = ajaxObj("POST", "index.php?remove_w");
        ajax.onreadystatechange = function () {
            if (ajaxReturn(ajax) === true) {
                if (ajax.responseText === "1") {
                    alert('Wallet removed successfully!');
                    window.location = "";
                } else if (ajax.responseText == "2") {
                    alert('Wallet does not exist. Reload page and try again.');
                } else if (ajax.responseText == "3") {
                    alert('User not found. Reload page and try again.');
                } else {
                    alert(ajax.responseText);

                }
                btn.disabled = false;
                btn.innerHTML = '<em class="icon ni ni-trash-alt"></em>';
            }
        };
        ajax.send("w_id=" + x);
    }

}

function check(x) {
    var ajax = ajaxObj("POST", "../controller/post.php");
    ajax.onreadystatechange = function () {
        if (ajaxReturn(ajax) === true) {
            if (ajax.responseText === "success") {
                ___('withdraw_btn').disabled = false;
                ___('amount').disabled = false;
            } else if (ajax.responseText == "0") {
                ___('withdraw_btn').disabled = true;
                ___('amount').disabled = true;
            } else {
                alert(ajax.responseText);
                ___('withdraw_btn').disabled = true;
                ___('amount').disabled = true;
            }
        }
    };
    ajax.send("from=" + x + "&function=check_balance");
}

function check_btn(x) {
    var terms = ___(x);
    if (terms.checked === false) {
        ___('btn-register').disabled = true;
    } else {
        ___('btn-register').disabled = false;
    }
}

function check_coin(x) {
    var xx = x.split("||")[0];
    if ("Alt_Coin" == xx) {
        ___('alt_coin').style.display = 'block';
        ___('coinname').style.display = 'block';
        ___('coinname').required = true;
    } else {
        ___('alt_coin').style.display = 'none';
        ___('coinname').style.display = 'none';
        ___('coinname').required = false;
    }
}

function check_selected(x) {
    var xx = x;
    if ("Bank" == xx) {
        ___('bank_holder').style.display = 'block';
        ___('account_details').required = true;
        ___('wallet_holder').style.display = 'none';
        ___('wallet').required = false;
    } else {
        ___('wallet_holder').style.display = 'block';
        ___('wallet').required = true;
        ___('bank_holder').style.display = 'none';
        ___('account_details').required = false;

    }
}