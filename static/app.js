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
    
    console.log(result)
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