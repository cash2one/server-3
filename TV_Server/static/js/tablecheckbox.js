/**
 * Created by sugar on 16/3/29.
 */
var list = new Array();

$(function(){

    function initTableCheckbox() {
        var $thr = $('table thead tr');
        var $checkAllTh = $('<th><input type="checkbox" id="checkAll" name="checkAll" /></th>');
        /*将全选/反选复选框添加到表头最前，即增加一列*/
        $thr.prepend($checkAllTh);
        /*“全选/反选”复选框*/
        var $checkAll = $thr.find('input');
        $checkAll.click(function(event){
            getSelectRow(this);
            /*将所有行的选中状态设成全选框的选中状态*/
            $tbr.find('input').prop('checked',$(this).prop('checked'));
            /*并调整所有选中行的CSS样式*/
            if ($(this).prop('checked')) {
                $tbr.find('input').parent().parent().addClass('warning');
            } else{
                $tbr.find('input').parent().parent().removeClass('warning');
            }
            /*阻止向上冒泡，以防再次触发点击操作*/
            event.stopPropagation();
        });
        /*点击全选框所在单元格时也触发全选框的点击操作*/
        $checkAllTh.click(function(){
            $(this).find('input').click();
        });
        var $tbr = $('table tbody tr');
        var $checkItemTd = $('<td><input type="checkbox" name="checkItem" /></td>');
        /*每一行都在最前面插入一个选中复选框的单元格*/
        $tbr.prepend($checkItemTd);
        /*点击每一行的选中复选框时*/
        $tbr.find('input').click(function(event){
            getSelectRow(this)

            /*调整选中行的CSS样式*/
            $(this).parent().parent().toggleClass('warning');
            /*如果已经被选中行的行数等于表格的数据行数，将全选框设为选中状态，否则设为未选中状态*/
            $checkAll.prop('checked',$tbr.find('input:checked').length == $tbr.length ? true : false);
            /*阻止向上冒泡，以防再次触发点击操作*/
            event.stopPropagation();
        });
        /*点击每一行时也触发该行的选中操作*/
        $checkItemTd.click(function(){
            $(this).find('input').click();
        });
    }
    initTableCheckbox();





    Array.prototype.removeByValue = function(val) {
        for(var i=0; i<this.length; i++) {
            if(this[i] == val) {
            this.splice(i, 1);
            break;
            }
        }
    }

    Array.prototype.contains = function(obj) {
        var i = this.length;
        while (i--) {
            if (this[i] === obj) {
                return true;
            }
        }
        return false;
    }


  

    function getSelectRow(obj) {
        var single_row = obj.parentNode.parentNode;
        var index = single_row.rowIndex;
        var row_id = single_row.getAttribute("id");
        var checked = obj.checked;
        if (index == 0 && checked){
            list = [];
            var rows = single_row.parentNode.parentNode.rows;
            for(var i = 1;i<rows.length;i++){
                var row = rows[i];
                list.push(row);
            }
        }
        else if (index == 0 && !checked){
            list = [];
        }
        else if (index > 0 && checked){
            if (!list.contains(single_row)){
                list.push(single_row);
            }
        }
        else if (index > 0 && !checked){
            if (list.contains(single_row)){
                list.removeByValue(single_row);
            }
        }
    }


});

function editRow(){
    if (list.length == 1){
        $('#base_modal').modal({
            show:true,
            backdrop:'static'
        })
        var data = list[0];


        console.log("data==",data);
    }
    else {
        alert("请选择一项");
    }
}

function deleteRow() {
    if (list.length == 0){
        alert("请选择至少一项");
    }
    else {
        var ids = new Array();
        for(var i = 0;i<list.length;i++){
            var row = list[i].getAttribute('id');
            ids.push(row);

        }

        $.ajax({
            url : "/backend/delete_data/",
            type : "GET",
            dataType: "json",
            timeout:8000,
            data : {item:ids},
            traditional: true, 
            beforeSend:function () {
                $("#loading").show();
            },
            success : function(data) {
                console.log("11")
                window.location.reload();
            },
            error : function(xhr,errmsg,err) {
                
            }
        });
    }
}