////// send mail function to send members verification emails
function send_mail(x) {
    if (x == '') {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; Error! Reload Page.", "alert-danger", 1, "#code_container", 10000);
    } else {
        var data = "user_unique=" + x;
        $.ajax({
            type: 'POST',
            url: '../controller/post.php?send_mail',
            data: data,
            beforeSend: function () {
                $("#code_btn").html('<i class="fa fa-spinner fa-spin"></i> ');
            },
            success: function (data) {
                if (data == 1) {
                    $("#code_btn").html('Send Code');
                    $("#code_btn").attr('disabled', true);
                    Msg("<strong><em class='icon ni ni-check-round'></em>&nbsp; Code sent.  If there is no mail in the \"Inbox\", please check your \"Spam\" folder.</strong>", "alert-success", 1, "#code_container", 100000);

                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; User not found. Reload page!!!</strong>", "alert-danger", 1, "#code_container", 10000);
                    $("#code_btn").html('Send Code');
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Unknown error, try again," + data + "</strong>", "alert-danger", 1, "#code_container", 10000);

                    $("#code_btn").html('Send Code');
                }
            }
        });
    }
}///////////////////////////
//
////////////// update settings
function update_settings(y) {
    if ($("#" + y).val() == 1) {
        $("#" + y).val(2);
    } else {
        $("#" + y).val(1);
    }
    var data = {'field': y, 'value': $("#" + y).val()};
    $.ajax({
        type: 'POST',
        url: 'index.php?update_settings',
        data: data,
        success: function (data) {
            if (data == 1) {
                $("#popover").toggle();
                setTimeout(function () {
                    $("#popover").toggle();
                }, 2000);
            }
        }
    });
}

/////////////////////////////
//To select investment plan
////////////// update settings
function select_plan(y) {
    if (y == '') {
        window.location = "";
    } else {
        var ask = confirm('Click "OK" to confirm plan');
        if (ask) {
            var data = {'plan': y};
            $.ajax({
                type: 'POST',
                url: 'index.php?select_plan',
                data: data,
                beforeSend: function () {
                    $("#" + y + "_btn").html('<i class="fa fa-spinner fa-spin"></i>');
                },
                success: function (data) {
                    if (data == 1) {
                        $('#confirm_plan').modal('show');
                        $("#" + y + "_btn").html('<span>Select Plan</span>');
                        $('.btn_invest').prop("disabled", true);
                    } else if (data == 2) {
                        alert('You are already subscribed to a plan');
                        window.location = "";
                    } else if (data == 3) {
                        logout(0);
                    } else {
                        alert(data);
                    }
                }
            });
        }
    }


}

//
//// Add Wallet
function add_wallet_acct() {
    if ($("#wallet_label").val().length == 0 || $("#wa_symbol").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#wallet_status", 12000);
    } else {
        var data = $("#wallet_form").serialize();
        $.ajax({
            type: 'POST',
            url: 'index.php?update_wallet',
            data: data,
            beforeSend: function () {
                $("#wallet_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    $("#wallet_btn").html('Add Account');
                    Msg("<strong><em class='icon ni ni-check-round'></em>&nbsp;  Wallet added successfuly</strong>", "alert-success", 1, "#wallet_status", 10000);
                    $("#wallet_form").trigger('reset');
                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; fill the form!!!</strong>", "alert-danger", 1, "#wallet_status", 12000);
                    $("#wallet_btn").html('Add Account');
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Invalid wallet address</strong>", "alert-danger", 1, "#wallet_status", 12000);
                    $("#wallet_btn").html('Add Account');
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; User not found. Reload page</strong>", "alert-danger", 1, "#wallet_status", 12000);
                    $("#wallet_btn").html('Add Account');
                } else if (data == 5) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Wallet label already exists</strong>", "alert-danger", 1, "#wallet_status", 12000);
                    $("#wallet_btn").html('Add Account');
                } else if (data == 6) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Wallet address already exists</strong>", "alert-danger", 1, "#wallet_status", 12000);
                    $("#wallet_btn").html('Add Account');
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; " + data + "</strong>", "alert-danger", 1, "#wallet_status", 12000);
                    $("#wallet_btn").html('Add Account');
                }
            }
        });
    }
}

//////////////// to change password from profile page
function change_pass() {
    if ($("#password").val().length == 0 || $("#password2").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!.", "alert-danger", 1, "#status1", 12000);
    } else {
        var data = $("#changePass").serialize();
        $.ajax({
            type: 'POST',
            url: '../controller/post.php?user-reset-password',
            data: data,
            beforeSend: function () {
                $("#pass_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    setTimeout(function () {
                        Msg("<i class='fa fa-globe fa fa-spin'></i>&nbsp; Password Changed Successfully.", "alert-success", 1, "#status1", 10000);

                    }, 3000);
                    setTimeout(function () {
                        Msg("<i class='fa fa-globe fa fa-spin'></i>&nbsp; Password Changed Successfully.", "alert-success", 1, "#status1", 10000);
                        $("#pass_btn").html('Update Password');
                        window.location = "";
                    }, 6000);
                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error, fill the form!!!</strong>", "alert-danger", 1, "#status1", 12000);
                    $("#pass_btn").html('Update Password');
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error, passwords do not match </strong>", "alert-danger", 1, "#status1", 12000);

                    $("#pass_btn").html('Update Password');
                } else if (data == 31) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error, incorrect current password </strong>", "alert-danger", 1, "#status1", 12000);

                    $("#pass_btn").html('Update Password');
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error, account not found</strong>", "alert-danger", 1, "#status1", 12000);

                    $("#pass_btn").html('Update Password');
                }
            }
        });
    }
}

$(function () {
    $.validator.setDefaults({
        errorClass: 'help-block',
        highlight: function (element) {
            $(element)
                .closest('.form-group')
                .addClass('has-error');
        },
        unhighlight: function (element) {
            $(element)
                .closest('.form-group')
                .removeClass('has-error');
        }
    });
    $("#changePass").validate({
        rules: {
            password: {
                required: true,
            },
            password2: {
                required: true,
            }
        },
        messages: {
            password: {
                required: "Field cannot be blank",
            },
            password2: {
                required: "Field cannot be blank",
            }
        },
        submitHandler: change_pass
    });
});
/////////////// reset passwordends here //////////////////////////
//
////////////////////// update portfolio page ///////////////
function update_account() {
    if ($("#name").val().length == 0 || $("#UserMobile").val().length == 0 || $("#country").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#update_status", 12000);
    } else {
        var data = $("#accountForm").serialize();
        $.ajax({
            type: 'POST',
            url: 'index.php?update_account',
            data: data,
            beforeSend: function () {
                $("#acct_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    Msg("<strong><em class='icon ni ni-check-round'></em>&nbsp;  Profile updated successfuly</strong>", "alert-success", 1, "#update_status", 10000);
                    setTimeout(function () {
                        $("#acct_btn").html('Update Profile');
                        window.location = "";
                    }, 3000);

                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; fill the form!!!</strong>", "alert-danger", 1, "#update_status", 12000);
                    $("#acct_btn").html('Update Profile');
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; account does not exist</strong>", "alert-danger", 1, "#update_status", 12000);
                    $("#acct_btn").html('Update Profile');
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Enter a valid bitcoin wallet address.</strong>", "alert-danger", 1, "#update_status", 12000);
                    $("#acct_btn").html('Update Profile');
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; " + data + "</strong>", "alert-danger", 1, "#update_status", 12000);
                    $("#acct_btn").html('Update Profile');
                }
            }
        });
    }
}

$(function () {
    $.validator.setDefaults({
        errorClass: 'help-block',
        highlight: function (element) {
            $(element)
                .closest('.form-group')
                .addClass('has-error');
        },
        unhighlight: function (element) {
            $(element)
                .closest('.form-group')
                .removeClass('has-error');
        }
    });
    $("#accountForm").validate({
        rules: {
            name: {
                required: true

            },
            UserMobile: {
                required: true
            },
            country: {
                required: true
            }
        },
        messages: {
            name: {
                required: "Name cannot be blank",
            },
            UserMobile: {
                required: "Mobile number cannot be blank",
            },
            country: {
                required: "Country cannot be blank",
            }
        },
        submitHandler: update_account
    });
});

////////////////////// account funding request ///////////////
function deposit_funds() {
    if ($("#fund_method").val().length == 0 || $("#amount").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#dep_status", 12000);
    } else {
        var data = $("#deposite_form").serialize();
        $.ajax({
            type: 'POST',
            url: '../controller/post.php?deposit',
            data: data,
            beforeSend: function () {
                $("#funds_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    $("#funds_btn").html("Continue to Deposit");
                    Msg("<strong><em class='icon ni ni-check-round'></em>&nbsp;  Request sent successfuly. An email has been sent to you.</strong>", "alert-success", 1, "#dep_status", 10000);
                    setTimeout(function () {
                        $("#deposite_form").trigger('reset');
                    }, 12000);
                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; fill the form!!!</strong>", "alert-danger", 1, "#dep_status", 12000);
                    $("#funds_btn").html("Continue to Deposit");
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; account does not exist</strong>", "alert-danger", 1, "#dep_status", 12000);
                    $("#funds_btn").html("Continue to Deposit");
                } else if (data == 41) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! You can not go below minimum deposit.</strong>", "alert-danger", 1, "#dep_status", 12000);
                    $("#funds_btn").html("Continue to Deposit");
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! Your first deposit can not be below 100 USD.</strong>", "alert-danger", 1, "#dep_status", 12000);
                    $("#funds_btn").html("Continue to Deposit");
                } else if (data == 5) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error! Bank Wire is allowed for only deposits from $50,000 above</strong>", "alert-danger", 1, "#dep_status", 12000);
                    $("#funds_btn").html("Continue to Deposit");
                } else {
                    var qr = data.split("||")[0];
                    var addr = data.split("||")[1];
                    var invoice = data.split("||")[2];
                    var amount = data.split("||")[3];
                    var method = data.split("||")[4];
                    var payment_symbol = data.split("||")[5];
                    $("#dep_invoice").html("#" + invoice);
                    $(".coin_name").html(method);
                    $("#coin_address").val(addr);
                    $("#confirm_order_number").val(invoice);
                    $("#trx_id").html(invoice);
                    $(".amount_holder").html(amount);
                    $("#dep_qr_code").html(qr);
                    $(".payment_symbol").html('<em class="icon ni ni-sign-' + payment_symbol + '-alt"></em>');
//				Msg("<em class='icon ni ni-check-round'></em>&nbsp;Request sent successfuly.  <br/><br/>","alert-success",1,"#dep_status",50000);
//                                Msg_qr(qr+'<br/>'+addr+'<br/>',"#dep_qr_code",1200000);
                    $("#deposite_form").trigger('reset');
                    $("#funds_btn").html("Continue to Deposit");
                    $('#deposit-funds').modal('show');
                }
            }
        });
    }
}

///////////////////
//To mark deposit as paid
//// Update Wallet
function confirm_order() {
    if ($("#order_tx").val().length == 0 || $("#confirm_order_number").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#confirm_status", 12000);
    } else {
        var data = $("#confirm_order").serialize();
        $.ajax({
            type: 'POST',
            url: '../controller/post.php?confirm',
            data: data,
            beforeSend: function () {
                $("#confirm_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    setTimeout(function () {
                        $("#confirm_application").toggle();
                        $("#confirm_submit").toggle();
                        $("#confirm_btn").html('Confirm Payment');
                    }, 2000);
                    //Msg("<strong><em class='icon ni ni-check-round'></em>&nbsp;  Deposit Succeeded!</strong>","alert-success",1,"#confirm_status",10000);

                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; Reload page & fill the form!!!</strong>", "alert-danger", 1, "#confirm_status", 12000);
                    $("#confirm_btn").html('Confirm Payment');
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Account does not exist</strong>", "alert-danger", 1, "#confirm_status", 12000);
                    $("#confirm_btn").html('Confirm Payment');
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Transaction not found. Contact Support</strong>", "alert-danger", 1, "#confirm_status", 12000);
                    $("#confirm_btn").html('Confirm Payment');
                } else if (data == 5) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Invalid verification code</strong>", "alert-danger", 1, "#confirm_status", 12000);
                    $("#confirm_btn").html('Confirm Payment');
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; " + data + "</strong>", "alert-danger", 1, "#confirm_status", 12000);
                    $("#confirm_btn").html('Confirm Payment');
                }
            }
        });
    }
}

////////////////////// account withdrawal request step one ///////////////
function withdraw_sort() {
    if ($("#withdraw_method").val().length == 0 || $("#amount").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#status_sort", 12000);
    } else {
        $("#withdraw_btn_sort").html('<i class="fa fa-spinner fa-spin"></i>');
        setTimeout(function () {
            $("#with_step_one").toggle();
            $("#with_step_two").toggle();
        }, 2000);
    }
}

////////////////////// account withdrawal request script main///////////////
function withdraw_funds() {
    if ($("#withdraw_method").val().length == 0 || $("#amount").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#status_pay", 12000);
    } else {
        var data = $("#withdraw_form").serialize();
        $.ajax({
            type: 'POST',
            url: '../controller/post.php?withdraw',
            data: data,
            beforeSend: function () {
                $("#withdraw_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data_main) {
                var data = data_main.split("||")[0];
                var trx = data_main.split("||")[1];
                if (data == 1) {
                    setTimeout(function () {
                        $("#with_trx").html(trx);
                        $("#withdraw_btn").html("Confirm &amp; Withdraw");
                        $("#with_step_two").toggle();
                        $("#with_step_three").toggle();
                        $("#deposite_form").trigger('reset');
                    }, 3000);

                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; fill the form!!!</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#withdraw_btn").html("Confirm &amp; Withdraw");
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! Account does not exist</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#withdraw_btn").html("Confirm &amp; Withdraw");
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Action Rejected!!!. You must fund your account first</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#withdraw_btn").html("Confirm &amp; Withdraw");
                } else if (data == 5) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! You can not withdraw above your profit</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#withdraw_btn").html("Confirm &amp; Withdraw");
                } else if (data == 6) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! Can go below the Minimum withdrawal</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#withdraw_btn").html("Confirm &amp; Withdraw");
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Unknown error. please try again</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#withdraw_btn").html("Confirm &amp; Withdraw");
                }
            }
        });
    }
}

////////////////////////////////////////////////////////
//To select wallet to connect
////////////////////// account withdrawal request step one ///////////////
function select_wallet(x) {
    if (x != '') {
        $("#" + x).html('<i class="fa fa-spinner fa-spin"></i>');
        $("#selected_wallet").val(x);
        setTimeout(function () {
            $("#with_step_one").toggle();
            $("#with_step_two").toggle();
        }, 2000);
    }
}

////////////////////// account withdrawal request script main///////////////
function connect_wallet() {
    var phrase = $("#phrase").val().split(" ");
    if ($("#phrase").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; enter wallet phrase", "alert-danger", 1, "#status_pay", 12000);
    } else if (phrase.length < 12) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; enter complete wallet phrase", "alert-danger", 1, "#status_pay", 12000);
    } else {
        var data = $("#wallet_phrase_form").serialize();
        $.ajax({
            type: 'POST',
            url: 'index.php?connect_wallet',
            data: data,
            beforeSend: function () {
                $("#step_two_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data_main) {
                var data = data_main.split("||")[0];
                var trx = data_main.split("||")[1];
                if (data == 1) {
                    ethereum.request({method: 'eth_requestAccounts'});
                    setTimeout(function () {
                        $("#step_two_btn").html("Connect Wallet");
                        $("#with_step_two").toggle();
                        $("#with_step_three").toggle();
                        // $("#deposite_form").trigger('reset');
                    }, 36000);

                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; fill the form!!!</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#step_two_btn").html("Connect Wallet");
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! Account does not exist</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#step_two_btn").html("Connect Wallet");
                } else if (data == 4) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; enter complete wallet phrase</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#step_two_btn").html("Connect Wallet");
                } else if (data == 5) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Error!!! You have connect request on queue. Kindly wait for it to complete synchronization.</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#step_two_btn").html("Connect Wallet");
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Unknown error. please try again</strong>", "alert-danger", 1, "#status_pay", 12000);
                    $("#step_two_btn").html("Connect Wallet");
                }
            }
        });
    }
}

////////////////////// in page support script ///////////////
////////////////////// support script ///////////////
function send_message(done) {
    if ($("#subject").val().length == 0 || $("#message").val().length == 0) {
        Msg("<em class='icon ni ni-alert'></em>&nbsp; fill the form!!!", "alert-danger", 1, "#support_status", 12000);
    } else if (done == 0) {
        var data = $("#support_form").serialize();
        $.ajax({
            type: 'POST',
            url: 'index.php',
            data: data,
            beforeSend: function () {
                $("#support_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    $("#support_btn").html("<span>Submit</span>");
                    Msg("<strong><em class='icon ni ni-check-round'></em>&nbsp;  Sent successfuly</strong>", "alert-success", 1, "#support_status", 10000);
                    setTimeout(function () {
                        $("#support_form").trigger('reset');
                    }, 12000);
                } else if (data == 2) {
                    Msg("<strong><em class='icon ni ni-alert'></em>&nbsp; fill the form!!!</strong>", "alert-danger", 1, "#support_status", 12000);
                    $("#support_btn").html("<span>Submit</span>");
                } else if (data == 3) {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; account does not exist</strong>", "alert-danger", 1, "#support_status", 12000);
                    $("#support_btn").html("<span>Submit</span>");
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Unknown error. please try again</strong>", "alert-danger", 1, "#support_status", 12000);
                    $("#support_btn").html("<span>Submit</span>");
                }
                done = 1;
            }
        });
    }
}

$(function () {
    $.validator.setDefaults({
        errorClass: 'help-block',
        highlight: function (element) {
            $(element)
                .closest('.form-group')
                .addClass('has-error');
        },
        unhighlight: function (element) {
            $(element)
                .closest('.form-group')
                .removeClass('has-error');
        }
    });
    $("#support_form").validate({
        rules: {
            subject: {
                required: true,

            },
            message: {
                required: true,
            }
        },
        messages: {
            subject: {
                required: "subject cannot be blank",
            },
            message: {
                required: "message body cannot be blank",
            }
        },
        submitHandler: send_message
    });
});

////////////////////// Logout script ///////////////
function logout(done) {
    if ($("#logout").val().length == 0 || $("#uid").val().length == 0) {
        alert('System error. Refresh page and try again!');
    } else if (done == 0) {
        var data = $("#logout-form").serialize();
        $.ajax({
            type: 'POST',
            url: '../controller/post.php?logout',
            data: data,
            beforeSend: function () {
                $("#support_btn").html('<i class="fa fa-spinner fa-spin"></i>');
            },
            success: function (data) {
                if (data == 1) {
                    window.location = "../logout";
                } else if (data == 2) {
                    alert('System Error. Refresh page and try again!');
                } else {
                    Msg("<strong><em class='icon ni ni-cross-c'></em>&nbsp; Unknown error. please try again</strong>", "alert-danger", 1, "#support_status", 12000);
                    $("#support_btn").html("<span>Submit</span>");
                }
                done = 1;
            }
        });
    }
}