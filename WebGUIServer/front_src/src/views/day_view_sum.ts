import m from "mithril"
import EventFill from "./eventfill.ts"
console.log(EventFill)
function GetDayInfo() {
  //Create fetch
  //Create children
}
let dummyData = {
  0: {
    msg:"Hello"
  },
  1: {
    msg:"Hello"
  },
  2: {
    msg:"Hello"
  }
}
var DaySum = {
  view: function() {
    return m("div", {class: "day_sum_view"},[
      m("nav", [
        m("button", "next"),
        m("button", "previous")
      ]),
      m("div", {class: "eventfill"},
        Object.entries(dummyData).map(x=>m(EventFill, {id:x[0],data:x[1]}))  
      )
    ])
  }
} 
export default DaySum
