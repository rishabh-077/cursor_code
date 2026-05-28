let state = null;
let saveTimer = null;

const $ = (sel) => document.querySelector(sel);
const statusEl = $("#saveStatus");

async function load() {
  const res = await fetch("/api/progress");
  state = await res.json();
  render();
  renderStats();
}

async function save() {
  statusEl.textContent = "Saving…";
  statusEl.className = "save-status saving";
  try {
    const res = await fetch("/api/progress", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(state),
    });
    const data = await res.json();
    statusEl.textContent = `Saved ${formatTime(data.lastUpdated)}`;
    statusEl.className = "save-status";
    renderStats();
  } catch {
    statusEl.textContent = "Save failed";
    statusEl.className = "save-status error";
  }
}

function scheduleSave() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(save, 400);
}

function formatTime(iso) {
  if (!iso) return "";
  try {
    return new Date(iso).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  } catch {
    return "";
  }
}

function showToast(msg) {
  let t = document.querySelector(".toast");
  if (!t) {
    t = document.createElement("div");
    t.className = "toast";
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.classList.add("show");
  setTimeout(() => t.classList.remove("show"), 2800);
}

async function renderStats() {
  const res = await fetch("/api/stats");
  const s = await res.json();
  const pct = (d, t) => (t ? Math.round((d / t) * 100) : 0);

  $("#statsGrid").innerHTML = `
    <div class="stat-card">
      <div class="label">LeetCode</div>
      <div class="value">${s.leetcode.done}/${s.leetcode.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.leetcode.done, s.leetcode.total)}%"></div></div>
    </div>
    <div class="stat-card">
      <div class="label">SQL 50</div>
      <div class="value">${s.sql50.done}/${s.sql50.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.sql50.done, s.sql50.total)}%"></div></div>
    </div>
    <div class="stat-card">
      <div class="label">Exit checklist</div>
      <div class="value">${s.exit.done}/${s.exit.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.exit.done, s.exit.total)}%"></div></div>
    </div>
    <div class="stat-card">
      <div class="label">Daily blocks</div>
      <div class="value">${s.blocks.done}/${s.blocks.total}</div>
      <div class="bar"><div class="bar-fill" style="width:${pct(s.blocks.done, s.blocks.total)}%"></div></div>
    </div>
  `;
}

function render() {
  const w = state.week1;
  renderDays(w.days);
  renderLeetcode(w.leetcode);
  renderSql(w.sql50);
  renderDe(w.deTopics);
  renderExit(w.exitChecklist);
  renderOverviewExit(w.exitChecklist);
  renderReflection(w.reflection);
}

function renderDays(days) {
  $("#daysList").innerHTML = days
    .map(
      (d, i) => `
    <div class="card ${d.blockA && d.blockB && d.blockC ? "done" : ""}" data-day="${i}">
      <div class="card-body">
        <div class="card-title">${d.date} · ${d.day}</div>
        <div class="day-blocks">
          <label><input type="checkbox" data-field="blockA" ${d.blockA ? "checked" : ""} /> A · DSA</label>
          <label><input type="checkbox" data-field="blockB" ${d.blockB ? "checked" : ""} /> B · DE</label>
          <label><input type="checkbox" data-field="blockC" ${d.blockC ? "checked" : ""} /> C · Theory</label>
        </div>
        <textarea class="day-notes" data-field="notes" rows="1">${escapeHtml(d.notes || "")}</textarea>
      </div>
    </div>`
    )
    .join("");

  $("#daysList").querySelectorAll("[data-day]").forEach((el) => {
    const i = +el.dataset.day;
    el.querySelectorAll("input, textarea").forEach((inp) => {
      inp.addEventListener("change", () => {
        const field = inp.dataset.field;
        if (field === "notes") state.week1.days[i].notes = inp.value;
        else state.week1.days[i][field] = inp.checked;
        scheduleSave();
        renderStats();
      });
    });
  });
}

function renderLeetcode(items) {
  $("#leetcodeList").innerHTML = items
    .map(
      (p, i) => `
    <div class="card ${p.done ? "done" : ""}" data-lc="${i}">
      <div class="card-body">
        <div class="card-title">
          <a href="https://leetcode.com/problems/${p.slug}/" target="_blank" rel="noopener">${p.id}. ${p.title}</a>
        </div>
        <div class="card-meta">${p.pattern}</div>
        <div class="card-subchecks">
          <label><input type="checkbox" data-field="done" ${p.done ? "checked" : ""} /> Solved</label>
          <label><input type="checkbox" data-field="noHints" ${p.noHints ? "checked" : ""} /> No hints</label>
          <label><input type="checkbox" data-field="complexityInRepo" ${p.complexityInRepo ? "checked" : ""} /> Notes in repo</label>
        </div>
      </div>
    </div>`
    )
    .join("");

  bindSubchecks("#leetcodeList", "leetcode");
}

function renderSql(items) {
  $("#sqlList").innerHTML = items
    .map(
      (s, i) => `
    <div class="card ${s.done ? "done" : ""}" data-sql="${i}">
      <input type="checkbox" data-field="done" ${s.done ? "checked" : ""} />
      <div class="card-body">
        <div class="card-title">
          <a href="https://leetcode.com/problems/${s.slug}/" target="_blank" rel="noopener">#${s.num} · ${s.title}</a>
        </div>
        <div class="card-meta">LC ${s.lc} · ${s.section}</div>
      </div>
    </div>`
    )
    .join("");

  $("#sqlList").querySelectorAll("[data-sql]").forEach((el) => {
    const i = +el.dataset.sql;
    el.querySelector("input").addEventListener("change", (e) => {
      state.week1.sql50[i].done = e.target.checked;
      scheduleSave();
      render();
    });
  });
}

function renderDe(items) {
  $("#deList").innerHTML = items
    .map(
      (t, i) => `
    <div class="card ${t.done ? "done" : ""}" data-de="${i}">
      <input type="checkbox" data-field="done" ${t.done ? "checked" : ""} />
      <div class="card-body">
        <div class="card-title">${t.title}</div>
        ${t.path ? `<div class="card-meta">${t.path}</div>` : ""}
      </div>
    </div>`
    )
    .join("");

  $("#deList").querySelectorAll("[data-de]").forEach((el) => {
    const i = +el.dataset.de;
    el.querySelector("input").addEventListener("change", (e) => {
      state.week1.deTopics[i].done = e.target.checked;
      syncExitFromDe();
      scheduleSave();
      render();
    });
  });
}

function syncExitFromDe() {
  const de = state.week1.deTopics;
  const exit = state.week1.exitChecklist;
  const map = { "spark-de": "spark-de", "spark-lazy": "spark-lazy", "bq": "bq-select" };
  de.forEach((t) => {
    const exitId = map[t.id];
    const item = exit.find((e) => e.id === exitId);
    if (item) item.done = t.done;
  });
}

function renderExit(items) {
  $("#exitList").innerHTML = items
    .map(
      (e, i) => `
    <div class="card ${e.done ? "done" : ""}" data-exit="${i}">
      <input type="checkbox" ${e.done ? "checked" : ""} />
      <div class="card-body"><div class="card-title">${e.label}</div></div>
    </div>`
    )
    .join("");

  $("#exitList").querySelectorAll("[data-exit]").forEach((el) => {
    const i = +el.dataset.exit;
    el.querySelector("input").addEventListener("change", (ev) => {
      state.week1.exitChecklist[i].done = ev.target.checked;
      scheduleSave();
      render();
    });
  });
}

function renderOverviewExit(items) {
  $("#overviewExit").innerHTML = items
    .map((e) => `<div class="card ${e.done ? "done" : ""}" style="margin-bottom:0.4rem">
      <span style="margin-right:0.5rem">${e.done ? "✓" : "○"}</span>${e.label}
    </div>`)
    .join("");
}

function renderReflection(r) {
  $("#reflFinished").value = r.finished || "";
  $("#reflBlocked").value = r.blocked || "";
  $("#reflNext").value = r.nextWeek || "";
  $("#reflEnergy").value = r.energy || 0;
}

function bindSubchecks(container, key) {
  document.querySelector(container).querySelectorAll(`[data-lc]`).forEach((el) => {
    const i = +el.dataset.lc;
    el.querySelectorAll("input").forEach((inp) => {
      inp.addEventListener("change", () => {
        state.week1[key][i][inp.dataset.field] = inp.checked;
        if (key === "leetcode" && inp.dataset.field === "done") {
          const lc5 = state.week1.exitChecklist.find((e) => e.id === "lc5");
          if (lc5) {
            lc5.done = state.week1.leetcode.filter((p) => p.done).length >= 5;
          }
        }
        scheduleSave();
        render();
      });
    });
  });
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

document.querySelectorAll(".tab").forEach((tab) => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((t) => t.classList.remove("active"));
    document.querySelectorAll(".panel").forEach((p) => p.classList.remove("active"));
    tab.classList.add("active");
    $(`#panel-${tab.dataset.tab}`).classList.add("active");
  });
});

["reflFinished", "reflBlocked", "reflNext", "reflEnergy"].forEach((id) => {
  $(`#${id}`).addEventListener("input", () => {
    state.week1.reflection.finished = $("#reflFinished").value;
    state.week1.reflection.blocked = $("#reflBlocked").value;
    state.week1.reflection.nextWeek = $("#reflNext").value;
    state.week1.reflection.energy = +$("#reflEnergy").value || 0;
    scheduleSave();
  });
});

$("#syncBtn").addEventListener("click", async () => {
  await save();
  const res = await fetch("/api/sync-markdown", { method: "POST" });
  const data = await res.json();
  if (data.ok) showToast(`Synced → ${data.path}`);
});

load();
