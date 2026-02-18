// JS pour la page du flux dynamique
async function loadFlux() {
  const response = await fetch("/reviews/flux/data/");
  const data = await response.json();
  const container = document.getElementById("flux-list");
  container.innerHTML = '';
  data.flux.forEach(item => {
    const div = document.createElement('div');
    div.className = 'flux-item';
    div.innerHTML = `<div class="flux-header"><strong>${item.type}</strong> — <em>${item.author}</em> <span style="float:right; color:#888; font-size:0.9em;">${item.date}</span></div><div class="flux-content">${item.content}</div>`;
    container.appendChild(div);
  });
}
loadFlux();
setInterval(loadFlux, 30000);
