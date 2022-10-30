document.addEventListener("DOMContentLoaded", () => {
    let todaydate = document.getElementById("issuedate");
    let n =  new Date();
    let y = n.getFullYear();
    let m = n.getMonth() + 1;
    let d = n.getDate();
    if(m < 10)
    m = '0' + m.toString();
    else if(d < 10)
    d = '0' + d.toString();

    let maxDate = y + '-' + m + '-' + d
    if (todaydate) {
        todaydate.setAttribute("max",maxDate);
        todaydate.setAttribute("value",maxDate);
    }

    setTimeout(fade_out, 10000);

    var selectcurr = document.getElementById("project-currency");
    if (selectcurr) {
        var optioncurr = selectcurr.options[selectcurr.selectedIndex];
        var attrcur = optioncurr.getAttribute("data-sym");
    }
    var gt = document.getElementById("grandtotal");
    if (selectcurr && gt) {
        gt.innerHTML = `Grand Total (${attrcur})`;
    }

    let tableItem = document.getElementById("item-entries")
    if (tableItem) {
        rowidx = tableItem.rows.length - 2;
    }
});

var rowidx = rowidx

function fade_out() {
    $(".message").fadeOut().empty();
}

function addpercentrow() {
    var total_percent = 0;
    var table = document.getElementById("percent-table");
    var rowCount = table.rows.length;
    for (var i = 0; i < table.rows.length; i++) {
        percent = table.rows[i].cells[0].firstChild.value;
        if (percent) {
            total_percent = total_percent + parseInt(percent);
            if (total_percent > 100) {
                alert("More than 100%");
                table.rows[i].cells[0].firstChild.value = "";
            }
        }
    }
    if (total_percent < 100) {
        for (var i = 0; i < table.rows.length; i++) {
            percent = table.rows[i].cells[0].firstChild.value;
            if (percent) {
                if (i == table.rows.length-1) {
                    var row = table.insertRow(rowCount);
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    var newrow = rowCount + 1;
                    cell1.innerHTML = '<td><input name="percent[]" id="percent'+ newrow +'" type="number" onchange="addpercentrow(this)"></td>'
                    cell2.innerHTML = '<td>% upon</td>'
                    cell3.innerHTML = '<td><input name="remark[]" id="remark'+ newrow +'" type="text"></td>'
                    break
                }
            }
        }
    } else if (total_percent == 100) {
        for (var i = 0; i < table.rows.length; i++) {
            percent = table.rows[i].cells[0].firstChild.value;
            if (!percent) {
                table.deleteRow(i);
            }
        }
    } 
}

function calculategrandamount() {
    var table = document.getElementById("item-entries")
    var grandtotalamount = 0;
    for (var i = 2; i < table.rows.length - 1; i++) {
        amount = parseFloat(table.rows[i].cells[5].innerHTML);
        if (amount) {
            grandtotalamount = grandtotalamount + amount;
            document.getElementById("grandtotalamount").innerHTML = grandtotalamount.toFixed(2);
        }
    }
}

function calculatetotalprice(row) {
    if (row.parentElement.id.slice(0,8) == "quantity") {
        var row_id = row.parentElement.id.slice(8)
    } else {
        var row_id = row.parentElement.id.slice(9)
    }
    var qty = document.getElementById(`quantity${row_id}`).firstChild.value
    var unitprice = document.getElementById(`unitprice${row_id}`).firstChild.value
    qty = parseFloat(qty);
    unitprice = parseFloat(unitprice);
    if (qty && unitprice) {
        total = qty * unitprice;
        total_2 = total.toFixed(2);
        document.getElementById(`totalprice${row_id}`).innerHTML = total_2;
        calculategrandamount();
    }
}

function forwardcurrency() {
    var selectcurr = document.getElementById("project-currency");
    var optioncurr = selectcurr.options[selectcurr.selectedIndex];
    var attrcur = optioncurr.getAttribute("data-sym");
    var gt = document.getElementById("grandtotal");
    gt.innerHTML = `Grand Total (${attrcur})`;
}


function addrowitems() {
    var table = document.getElementById("item-entries")
    var tablebody = document.getElementById("item-entries").getElementsByTagName('tbody')[0];
    var rowCount = table.rows.length - 2;
    var row = tablebody.insertRow();
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
    var cell7 = row.insertCell(6);
    var newrow = rowidx + 1;
    cell2.innerHTML = '<input class="item-table" type="text" maxlength="50" name="item-description[]" required>';
    cell3.innerHTML = '<input class="item-table" type="number" min="0" step="any" name="item-quantity[]" onchange="calculatetotalprice(this)" required>';
    cell4.innerHTML = '<input class="item-table" type="text" maxlength="5" name="item-uom[]" required>';
    cell5.innerHTML = '<input class="item-table" id="input-unitprice' + newrow + '" min="0" step="any" type="number" name="item-unitprice[]" onchange="calculatetotalprice(this)" required>';
    cell6.innerHTML = '';
    cell7.innerHTML = '<button onclick="deleteitemrow(this)">Delete</button>';
    cell1.className = 'counterCell';
    cell2.id = 'description' + newrow;
    cell3.id = 'quantity' + newrow;
    cell4.id = 'uom' + newrow;
    cell5.id = 'unitprice' + newrow;
    cell6.id = 'totalprice' + newrow;
    cell7.id = 'delete' + newrow;
    rowidx ++;
}

function deleteitemrow(button) {
    var cell = button.parentElement;
    var row = cell.parentElement;
    row.parentNode.removeChild(row);
    calculategrandamount()
}


