const vessel_length = document.getElementById("vessellength")
const vessel_width = document.getElementById("vesselwidth")
const enterbtn = document.getElementById("enter-btn-all")
const deletebtn = document.getElementById("delete-btn-all")

const dock_name = document.getElementById("dockname")

const date_start = document.getElementById("startdate")
const date_end = document.getElementById("enddate")
const reasontext = document.getElementById("reason")

const alerttext = document.getElementById("alert")

const reservation_confirmation_page = document.getElementById("reservation-confirmation")
const confirmbtn = document.getElementById("confirm-reservation")
const unconfirmbtn = document.getElementById("unconfirm-reservation")

const reservation_confirmation_page_delete = document.getElementById("reservation-confirmation-delete")
const confirmbtn_resdelete = document.getElementById("confirm-reservation-delete")
const unconfirmbtn_resdelete = document.getElementById("unconfirm-reservation-delete")

const reservations_table = document.getElementById("reservations-table")

let selected_id

const create_reservation = function(rowsList) {
    for (row of rowsList) {
        const newRow = document.createElement("tr")
        const dock_col = document.createElement("th")
        const start_col = document.createElement("th")
        const end_col = document.createElement("th")
        const reason_col = document.createElement("th")
        const id_col = document.createElement("th")
        const deleterow_btn = document.createElement("button")
        deleterow_btn.classList.add("delete_reservation")
        deleterow_btn.id = row["id"]
        dock_col.textContent = row["dock_name"]
        start_col.textContent = row["start_date"]
        end_col.textContent = row["end_date"]
        reason_col.textContent = row["reason"]
        id_col.textContent = row["id"]
        deleterow_btn.textContent = "x"
        newRow.append(dock_col)
        newRow.append(start_col)
        newRow.append(end_col)
        newRow.append(reason_col)
        newRow.append(id_col)
        newRow.append(deleterow_btn)
        reservations_table.append(newRow)
    }
}
//create_reservation([{'id': 3, 'dock_number': 1, 'start_date': '2026-09-19', 'end_date': '2026-09-20', 'reason': 'yes'}])

async function loadReservations() {
    const response = await fetch('/api/reservations')
    const rows = await response.json()
    reservations_table.innerHTML = "" //clear old rows first
    create_reservation(rows)
    deleteButtons()
}

loadReservations()   

enterbtn.addEventListener('click', async () => {
    const response = await fetch('/api/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            dock_number: dock_name.value,
            length: vessel_length.value,
            width: vessel_width.value,
            start_date: date_start.value,
            end_date: date_end.value,
            reason: reasontext.value
        })
    });

    const result = await response.json()
    if (typeof result == "string") {
        alerttext.textContent = `error: ${result}`
    } else {
        alerttext.textContent = ""
        reservation_confirmation_page.classList.add("active")
        //window.alert("Reservation made, thank you.")
    }
    
    //console.log(result)
    console.log(dock_name.value)
    console.log(`${date_start.value}, ${date_end.value}`)
}) 

confirmbtn.addEventListener('click', async () => {
    const response = await fetch('/api/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            dock_number: dock_name.value,
            length: vessel_length.value,
            width: vessel_width.value,
            start_date: date_start.value,
            end_date: date_end.value,
            reason: reasontext.value,
            confirm_reservation: true
        })
    });

    reservation_confirmation_page.classList.remove("active")

    const result = await response.json()
    if (typeof result === "string") {
        alerttext.textContent = `error: ${result}`
    } else {
        await loadReservations()
    }
})

unconfirmbtn.addEventListener('click', () => {
    reservation_confirmation_page.classList.remove("active")
})

confirmbtn_resdelete.addEventListener('click', async () => {
    const response = await fetch('/api/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            reservation_id: selected_id,
            delete: true
        })
    });

    reservation_confirmation_page_delete.classList.remove("active")
    loadReservations()
})

unconfirmbtn_resdelete.addEventListener('click', () => {
    reservation_confirmation_page_delete.classList.remove("active")
})


function deleteButtons() {
    const delete_buttons = document.querySelectorAll('.delete_reservation');

    delete_buttons.forEach((btn, index) => {
        if (!btn.classList.value.includes("event-made")) {
            btn.addEventListener('click', async () => {
                selected_id = delete_buttons[index].id
                delete_buttons[index].classList.add("event-made")
                reservation_confirmation_page_delete.classList.add("active")
            });
        }

    });
}