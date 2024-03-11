import m from "mithril"
import "../default_event.less"
function EventFill() 
{ 
  return {
    oninit:function(){

    },
    view: function(vnode) {
      return m("div", {class: "event"}, [
        m("div",{class:"meta"},[
          m("div",vnode.attrs.id),
          m("button",[
            m("span","TIME")
          ])
        ]),
        m("div", {class:"data"},[
          m("span",JSON.stringify(vnode.attrs.data))
        ])
      ]) 
    }
  }
}
export default EventFill
