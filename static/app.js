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

const reservations_table = document.getElementById("reservations-table")

const create_reservation = function(rowsList) { //connect to backend
    for (row of rowsList) {
        const newRow = document.createElement("tr")
        const dock_col = document.createElement("th")
        const start_col = document.createElement("th")
        const end_col = document.createElement("th")
        const reason_col = document.createElement("th")
        const id_col = document.createElement("th")
        dock_col.textContent = row["dock_number"]
        start_col.textContent = row["start_date"]
        end_col.textContent = row["end_date"]
        reason_col.textContent = row["reason"]
        id_col.textContent = row["id"]
        newRow.append(dock_col)
        newRow.append(start_col)
        newRow.append(end_col)
        newRow.append(reason_col)
        newRow.append(id_col)
        reservations_table.append(newRow)
    }
}
create_reservation([{'id': 3, 'dock_number': 1, 'start_date': '2026-09-19', 'end_date': '2026-09-20', 'reason': 'yes'}])

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

deletebtn.addEventListener('click', async () => {
    const response = await fetch('/api/reservations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            dock_number: dock_name.value,
            start_date: date_start.value,
            end_date: date_end.value,
            delete: true
        })
    });
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
})

unconfirmbtn.addEventListener('click', () => {
    reservation_confirmation_page.classList.remove("active")
})