import { ToDoItem } from "./components/to-do-item.js";

const app = document.getElementById("app");

for (let i = 0; i < 5; i++) {
    app.appendChild(ToDoItem());
}
