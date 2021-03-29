//toast提示
$.extend({
    qtMessage: function (text, res, fun) {
        var f_color;
        var bground;
        if (res == '1') {
            f_color = '#00be6e';
            bground = '#f1fcf5';
        }else if (res == '0') {
            f_color = '#fd8320';
            bground = '#fff8f2';
        }else if (res == '-1') {
            f_color = '#fa5555';
            bground = '#fff5f5';
        }
        var messageName = 'message' + parseInt(Math.random() * 1000);
        $('body').append('<div class="' + messageName + '" style=" font-size: 14px;\n' +
            'display: none;' +
            'line-height: 1.5;\n' +
            'padding: 20px 30px;' +
            'border-radius: 4px;' +
            '-webkit-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);' +
            'box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);' +
            'background: ' + bground + ';' +
            'color: ' + f_color + ';\n' +
            'list-style: none;\n' +
            'position: fixed;\n' +
            'z-index: 2002;\n' +
            'transform: translateX(-50%);' +
            'top: 16px;\n' +
            'left: 50%;">' +
            text + '</div>');
        $('.' + messageName).fadeIn();
        setTimeout(function () {
            $('.' + messageName).fadeOut();
            $('.' + messageName).remove();
            if(fun)
                fun();
        }, 3000);
    }
});

//关闭jsreport
$('.j-model-close').click(function(){
        $(".js-report-t").fadeOut(200);
    })

//弹出jsreport
$('.j-model-open').click(function(){
        $(".js-report-t").fadeIn(200);
    });

//关闭jsreport
$('.console-model-close').click(function(){
        $(".console-report-t").fadeOut(200);
    })

//弹出jsreport
$('.console-model-open').click(function(){
        $(".console-report-t").fadeIn(200);
    });

setTimeout (function () {
            $(".sign-txt").hide();
        }, 3000);   //默认展示，3秒后自动关闭


//修改console log 测试的账号
$('#change_check_user').on('click', function() {
        var username, password;
        username = $('#username').val()
        password = $('#password').val()
        change_check_user(username, password, function(data, flag) {
            $.qtMessage(data, '1', function () {
                
            })
        });
    });

function change_check_user(username, password, callback) {
    var data = {
            "username": username,
            "password": password,
        }
    $.ajax({
            url: '/api/v1/fastest/console/change_check_user',
            type: 'post',
            dataType: 'json',
            data: JSON.stringify(data),
            success: function (res) {
                callback(res.data, true);
            },
            error: function(err) {
                callback(err.data, false);
            }
    });
}



//检测资源文件
$('#check_jscss').on('click', function() {

    check_source(function(res, flag) {
        if (flag) {
            if (res == '1') {
                var text = '进入待测列表，等待测试！';
            }else {
                var text = '正在测试中，请不要重复请求！';
            }
            $.qtMessage(text, res, function () {
                window.location.reload()
            })
        }
    });
});


function check_source(callback) {
    $.ajax({
        url: '/api/v1/fastest/check_source',
        type: 'post',
        success: function(res) {
            callback(res.message, true);
        },
        error: function(err) {
            callback(err, false);
        }
    });
}

//修改hosts
$('#submit').on('click', function() {
    let master_station = $('input[name="environment"]:checked').val();
    let dl_station = $('input[name="dl_environment"]:checked').val();
    let upload_station = $('input[name="upload_environment"]:checked').val();
    change_host(master_station, dl_station, upload_station, function(res, flag) {
        if (flag) {
            if (res == '1') {
                var text = '修改host成功!';
            }else {
                var text = '绑定失败，联系管理员！';
            }
            $.qtMessage(text, res, function () {

            })
        } else {
            alert("绑定失败，联系管理员！");
        }
    });
});
function change_host(master_station, dl_station, upload_station, callback) {
    $.ajax({
        url: '/api/v1/fastest/change_host',
        data: {
            master_station: master_station,
            dl_station: dl_station,
            upload_station: upload_station
        },
        type: 'post',
        success: function(res) {
            callback(res.message, true);
        },
        error: function(err) {
            callback(err, false);
        }
    });
}


//检测页面加载是否报错

$('#check_console').on('click', function() {

    get_browser_console(function(res, flag) {
        if (flag) {
            if (res == '1') {
                var text = '进入待测列表，等待测试！';
            }else if(res == '0') {
                var text = '正在测试中，请不要重复请求！';
            }else if(res == '-1') {
                var text = '账号被封禁，或账号不存在!';
            }
            $.qtMessage(text, res, function () {
                window.location.reload()
            })
        }
    });
});
function get_browser_console(callback) {
    $.ajax({
        url: '/api/v1/fastest/get_browser_console',
        type: 'post',
        success: function(res) {
            callback(res.message, true);
        },
        error: function(err) {
            callback(err, false);
        }
    });
}