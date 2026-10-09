// App detail pages: click a screen to open it at full size.
const dialog = document.querySelector("#viewer");
if (dialog) {
  const image = dialog.querySelector("img");
  document.querySelectorAll("[data-image]").forEach((button) =>
    button.addEventListener("click", () => {
      image.src = button.dataset.image;
      image.alt = button.querySelector("img").alt;
      dialog.showModal();
    }),
  );
  document.querySelector("#close").addEventListener("click", () => dialog.close());
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) dialog.close();
  });
}

// Home: copy the contact address.
const copy = document.querySelector("[data-copy-email]");
if (copy)
  copy.addEventListener("click", async () => {
    const status = document.querySelector("#copy-status");
    try {
      await navigator.clipboard.writeText("oniaby@onischool.net");
      status.textContent = "Email address copied.";
    } catch {
      status.textContent = "Select and copy oniaby@onischool.net.";
    }
  });
