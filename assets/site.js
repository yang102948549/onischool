document.querySelectorAll("[data-demo]").forEach((demo) => {
  const tabs = [...demo.querySelectorAll('[role="tab"]')];
  function select(tab, focus = false) {
    tabs.forEach((item) => {
      const active = item === tab;
      item.setAttribute("aria-selected", String(active));
      item.tabIndex = active ? 0 : -1;
      demo.querySelector("#" + item.getAttribute("aria-controls")).hidden =
        !active;
    });
    if (focus) tab.focus();
  }
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => select(tab));
    tab.addEventListener("keydown", (event) => {
      let next;
      if (event.key === "ArrowDown" || event.key === "ArrowRight")
        next = (index + 1) % tabs.length;
      if (event.key === "ArrowUp" || event.key === "ArrowLeft")
        next = (index + tabs.length - 1) % tabs.length;
      if (event.key === "Home") next = 0;
      if (event.key === "End") next = tabs.length - 1;
      if (next !== undefined) {
        event.preventDefault();
        select(tabs[next], true);
      }
    });
  });
});
const copy = document.querySelector("[data-copy-email]");
if (copy)
  copy.addEventListener("click", async () => {
    const status = document.querySelector("#copy-status");
    try {
      await navigator.clipboard.writeText("oniaby@onischool.net");
      status.textContent = "메일 주소를 복사했어요.";
    } catch {
      status.textContent = "oniaby@onischool.net을 선택해 복사해 주세요.";
    }
  });
