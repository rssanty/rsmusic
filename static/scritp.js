document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('app');      // El botón con id="app"
    const urlInput = document.getElementById('url');    // El input con id="url"
    const statusElement = document.getElementById('status'); // <p> con id="status"

    button.addEventListener('click', () => {
        const url = urlInput.value;
        statusElement.textContent = 'Iniciado descargar...';

        fetch('/download', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        })
        .then(res => res.json())
        .then(data => {
            if (data.message) {
                statusElement.textContent = data.message;
            } else if (data.error) {
                statusElement.textContent = 'Error: ' + data.error;
            }
        })
        .catch(err => {
            statusElement.textContent = 'Error: ' + err.message;
        });
    });
});
