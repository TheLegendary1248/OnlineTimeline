import './style.less'
import './day_sum_view.less'
import m from "mithril"
import app from "./day_sum_view.html?raw"
import DaySum from './views/day_view_sum'
let root = document.querySelector("#app")
m.mount( root, 
  DaySum
)
