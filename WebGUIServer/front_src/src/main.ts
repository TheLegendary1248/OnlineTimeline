import './style.less'
import './day_sum_view.less'

customElements.define(
  "unhandled-event-view",
  class extends HTMLElement {
    constructor() {
      super();
    }
    init(prop){
      this.prop = prop
      if(this.isConnected) this.render()
    }
    render(){
      if(this.prop == null) return
      let para = this.querySelector("p")
      console.log(para)
      para.textContent = JSON.stringify(this.prop)
    }
    connectedCallback(){
      let template = document.getElementById("template")?.content
      let clone = template.cloneNode(true)
      // const shadowroot = this.attachShadow({mode: "open"})
      this.appendChild(clone) 
      //Default style of all web components is inline
      //possibly change because it's an element style and could be a challenge to override
      this.style.display = "block"
      this.render()
    }
  }
)
customElements.define(
  "day-summary-view",
  class extends HTMLElement {
    constructor() {
      super();
    }
    connectedCallback(){
      //TODO capture day info
      let template = document.getElementById("day-summary-view")?.content
      let clone = template.cloneNode(true)
      // const shadowroot = this.attachShadow({mode: "open"})
      this.appendChild(clone) 
      //Default style of all web components is inline
      //possibly change because it's an element style and could be a challenge to override
      this.style.display = "block"

      //get the start of today
      let day = new Date
      day.setMilliseconds(0)
      day.setSeconds(0)
      day.setMinutes(0)
      day.setHours(0)

      this.querySelector(".date").textContent = `${day.getDate()}/${day.getMonth() + 1}/${day.getFullYear()}`
      this.day = day
      /*** @type HTMLButtonElement */
      this.querySelector(".next")
      .addEventListener("click", ()=>this.moveDate(true))
      this.querySelector(".previous")
      .addEventListener("click", ()=>this.moveDate(false))
      
    }
    moveDate(isForward){
      this.day = new Date(this.day.getTime() + (isForward ? 1 : -1) * 8.64e+7)
      this.querySelector(".date").textContent = `${this.day.getDate()}/${this.day.getMonth() + 1}/${this.day.getFullYear()}`
    }
  }
)
