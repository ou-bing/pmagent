import{b as B,h as g,g as d,f as A,r as C,x as M,a2 as O,u as N,ad as de,A as I,w as K,i as D,o as F,n as L,j as W,ae as Y,m as se}from"./bootstrap-Cg7-XUCZ.js";import{u as q}from"./use-merged-state-Bwrns1mu.js";import{i as le,r as _,B as j,d as H,h as p,c as V,U as ue}from"../jse/index-index-C-XMneWz.js";import{g as ce}from"./get-slot-Bk_rJcZu.js";const be=B("radio",`
 line-height: var(--n-label-line-height);
 outline: none;
 position: relative;
 user-select: none;
 -webkit-user-select: none;
 display: inline-flex;
 align-items: flex-start;
 flex-wrap: nowrap;
 font-size: var(--n-font-size);
 word-break: break-word;
`,[g("checked",[d("dot",`
 background-color: var(--n-color-active);
 `)]),d("dot-wrapper",`
 position: relative;
 flex-shrink: 0;
 flex-grow: 0;
 width: var(--n-radio-size);
 `),B("radio-input",`
 position: absolute;
 border: 0;
 width: 0;
 height: 0;
 opacity: 0;
 margin: 0;
 `),d("dot",`
 position: absolute;
 top: 50%;
 left: 0;
 transform: translateY(-50%);
 height: var(--n-radio-size);
 width: var(--n-radio-size);
 background: var(--n-color);
 box-shadow: var(--n-box-shadow);
 border-radius: 50%;
 transition:
 background-color .3s var(--n-bezier),
 box-shadow .3s var(--n-bezier);
 `,[C("&::before",`
 content: "";
 opacity: 0;
 position: absolute;
 left: 4px;
 top: 4px;
 height: calc(100% - 8px);
 width: calc(100% - 8px);
 border-radius: 50%;
 transform: scale(.8);
 background: var(--n-dot-color-active);
 transition: 
 opacity .3s var(--n-bezier),
 background-color .3s var(--n-bezier),
 transform .3s var(--n-bezier);
 `),g("checked",{boxShadow:"var(--n-box-shadow-active)"},[C("&::before",`
 opacity: 1;
 transform: scale(1);
 `)])]),d("label",`
 color: var(--n-text-color);
 padding: var(--n-label-padding);
 font-weight: var(--n-label-font-weight);
 display: inline-block;
 transition: color .3s var(--n-bezier);
 `),A("disabled",`
 cursor: pointer;
 `,[C("&:hover",[d("dot",{boxShadow:"var(--n-box-shadow-hover)"})]),g("focus",[C("&:not(:active)",[d("dot",{boxShadow:"var(--n-box-shadow-focus)"})])])]),g("disabled",`
 cursor: not-allowed;
 `,[d("dot",{boxShadow:"var(--n-box-shadow-disabled)",backgroundColor:"var(--n-color-disabled)"},[C("&::before",{backgroundColor:"var(--n-dot-color-disabled)"}),g("checked",`
 opacity: 1;
 `)]),d("label",{color:"var(--n-text-color-disabled)"}),B("radio-input",`
 cursor: not-allowed;
 `)])]),G={name:String,value:{type:[String,Number,Boolean],default:"on"},checked:{type:Boolean,default:void 0},defaultChecked:Boolean,disabled:{type:Boolean,default:void 0},label:String,size:String,onUpdateChecked:[Function,Array],"onUpdate:checked":[Function,Array],checkedValue:{type:Boolean,default:void 0}},J=de("n-radio-group");function Q(e){const o=le(J,null),t=M(e,{mergedSize(r){const{size:s}=e;if(s!==void 0)return s;if(o){const{mergedSizeRef:{value:u}}=o;if(u!==void 0)return u}return r?r.mergedSize.value:"medium"},mergedDisabled(r){return!!(e.disabled||o!=null&&o.disabledRef.value||r!=null&&r.disabled.value)}}),{mergedSizeRef:i,mergedDisabledRef:n}=t,c=_(null),b=_(null),h=_(e.defaultChecked),a=j(e,"checked"),m=q(a,h),x=O(()=>o?o.valueRef.value===e.value:m.value),w=O(()=>{const{name:r}=e;if(r!==void 0)return r;if(o)return o.nameRef.value}),v=_(!1);function k(){if(o){const{doUpdateValue:r}=o,{value:s}=e;I(r,s)}else{const{onUpdateChecked:r,"onUpdate:checked":s}=e,{nTriggerFormInput:u,nTriggerFormChange:l}=t;r&&I(r,!0),s&&I(s,!0),u(),l(),h.value=!0}}function R(){n.value||x.value||k()}function z(){R(),c.value&&(c.value.checked=x.value)}function S(){v.value=!1}function y(){v.value=!0}return{mergedClsPrefix:o?o.mergedClsPrefixRef:N(e).mergedClsPrefixRef,inputRef:c,labelRef:b,mergedName:w,mergedDisabled:n,renderSafeChecked:x,focus:v,mergedSize:i,handleRadioInputChange:z,handleRadioInputBlur:S,handleRadioInputFocus:y}}const he=Object.assign(Object.assign({},D.props),G),Ce=H({name:"Radio",props:he,setup(e){const o=Q(e),t=D("Radio","-radio",be,Y,e,o.mergedClsPrefix),i=V(()=>{const{mergedSize:{value:m}}=o,{common:{cubicBezierEaseInOut:x},self:{boxShadow:w,boxShadowActive:v,boxShadowDisabled:k,boxShadowFocus:R,boxShadowHover:z,color:S,colorDisabled:y,colorActive:r,textColor:s,textColorDisabled:u,dotColorActive:l,dotColorDisabled:f,labelPadding:$,labelLineHeight:P,labelFontWeight:T,[F("fontSize",m)]:U,[F("radioSize",m)]:E}}=t.value;return{"--n-bezier":x,"--n-label-line-height":P,"--n-label-font-weight":T,"--n-box-shadow":w,"--n-box-shadow-active":v,"--n-box-shadow-disabled":k,"--n-box-shadow-focus":R,"--n-box-shadow-hover":z,"--n-color":S,"--n-color-active":r,"--n-color-disabled":y,"--n-dot-color-active":l,"--n-dot-color-disabled":f,"--n-font-size":U,"--n-radio-size":E,"--n-text-color":s,"--n-text-color-disabled":u,"--n-label-padding":$}}),{inlineThemeDisabled:n,mergedClsPrefixRef:c,mergedRtlRef:b}=N(e),h=L("Radio",b,c),a=n?W("radio",V(()=>o.mergedSize.value[0]),i,e):void 0;return Object.assign(o,{rtlEnabled:h,cssVars:n?void 0:i,themeClass:a==null?void 0:a.themeClass,onRender:a==null?void 0:a.onRender})},render(){const{$slots:e,mergedClsPrefix:o,onRender:t,label:i}=this;return t==null||t(),p("label",{class:[`${o}-radio`,this.themeClass,this.rtlEnabled&&`${o}-radio--rtl`,this.mergedDisabled&&`${o}-radio--disabled`,this.renderSafeChecked&&`${o}-radio--checked`,this.focus&&`${o}-radio--focus`],style:this.cssVars},p("div",{class:`${o}-radio__dot-wrapper`}," ",p("div",{class:[`${o}-radio__dot`,this.renderSafeChecked&&`${o}-radio__dot--checked`]}),p("input",{ref:"inputRef",type:"radio",class:`${o}-radio-input`,value:this.value,name:this.mergedName,checked:this.renderSafeChecked,disabled:this.mergedDisabled,onChange:this.handleRadioInputChange,onFocus:this.handleRadioInputFocus,onBlur:this.handleRadioInputBlur})),K(e.default,n=>!n&&!i?null:p("div",{ref:"labelRef",class:`${o}-radio__label`},n||i)))}}),we=G,ke=H({name:"RadioButton",props:G,setup:Q,render(){const{mergedClsPrefix:e}=this;return p("label",{class:[`${e}-radio-button`,this.mergedDisabled&&`${e}-radio-button--disabled`,this.renderSafeChecked&&`${e}-radio-button--checked`,this.focus&&[`${e}-radio-button--focus`]]},p("input",{ref:"inputRef",type:"radio",class:`${e}-radio-input`,value:this.value,name:this.mergedName,checked:this.renderSafeChecked,disabled:this.mergedDisabled,onChange:this.handleRadioInputChange,onFocus:this.handleRadioInputFocus,onBlur:this.handleRadioInputBlur}),p("div",{class:`${e}-radio-button__state-border`}),K(this.$slots.default,o=>!o&&!this.label?null:p("div",{ref:"labelRef",class:`${e}-radio__label`},o||this.label)))}}),fe=B("radio-group",`
 display: inline-block;
 font-size: var(--n-font-size);
`,[d("splitor",`
 display: inline-block;
 vertical-align: bottom;
 width: 1px;
 transition:
 background-color .3s var(--n-bezier),
 opacity .3s var(--n-bezier);
 background: var(--n-button-border-color);
 `,[g("checked",{backgroundColor:"var(--n-button-border-color-active)"}),g("disabled",{opacity:"var(--n-opacity-disabled)"})]),g("button-group",`
 white-space: nowrap;
 height: var(--n-height);
 line-height: var(--n-height);
 `,[B("radio-button",{height:"var(--n-height)",lineHeight:"var(--n-height)"}),d("splitor",{height:"var(--n-height)"})]),B("radio-button",`
 vertical-align: bottom;
 outline: none;
 position: relative;
 user-select: none;
 -webkit-user-select: none;
 display: inline-block;
 box-sizing: border-box;
 padding-left: 14px;
 padding-right: 14px;
 white-space: nowrap;
 transition:
 background-color .3s var(--n-bezier),
 opacity .3s var(--n-bezier),
 border-color .3s var(--n-bezier),
 color .3s var(--n-bezier);
 background: var(--n-button-color);
 color: var(--n-button-text-color);
 border-top: 1px solid var(--n-button-border-color);
 border-bottom: 1px solid var(--n-button-border-color);
 `,[B("radio-input",`
 pointer-events: none;
 position: absolute;
 border: 0;
 border-radius: inherit;
 left: 0;
 right: 0;
 top: 0;
 bottom: 0;
 opacity: 0;
 z-index: 1;
 `),d("state-border",`
 z-index: 1;
 pointer-events: none;
 position: absolute;
 box-shadow: var(--n-button-box-shadow);
 transition: box-shadow .3s var(--n-bezier);
 left: -1px;
 bottom: -1px;
 right: -1px;
 top: -1px;
 `),C("&:first-child",`
 border-top-left-radius: var(--n-button-border-radius);
 border-bottom-left-radius: var(--n-button-border-radius);
 border-left: 1px solid var(--n-button-border-color);
 `,[d("state-border",`
 border-top-left-radius: var(--n-button-border-radius);
 border-bottom-left-radius: var(--n-button-border-radius);
 `)]),C("&:last-child",`
 border-top-right-radius: var(--n-button-border-radius);
 border-bottom-right-radius: var(--n-button-border-radius);
 border-right: 1px solid var(--n-button-border-color);
 `,[d("state-border",`
 border-top-right-radius: var(--n-button-border-radius);
 border-bottom-right-radius: var(--n-button-border-radius);
 `)]),A("disabled",`
 cursor: pointer;
 `,[C("&:hover",[d("state-border",`
 transition: box-shadow .3s var(--n-bezier);
 box-shadow: var(--n-button-box-shadow-hover);
 `),A("checked",{color:"var(--n-button-text-color-hover)"})]),g("focus",[C("&:not(:active)",[d("state-border",{boxShadow:"var(--n-button-box-shadow-focus)"})])])]),g("checked",`
 background: var(--n-button-color-active);
 color: var(--n-button-text-color-active);
 border-color: var(--n-button-border-color-active);
 `),g("disabled",`
 cursor: not-allowed;
 opacity: var(--n-opacity-disabled);
 `)])]);function ve(e,o,t){var i;const n=[];let c=!1;for(let b=0;b<e.length;++b){const h=e[b],a=(i=h.type)===null||i===void 0?void 0:i.name;a==="RadioButton"&&(c=!0);const m=h.props;if(a!=="RadioButton"){n.push(h);continue}if(b===0)n.push(h);else{const x=n[n.length-1].props,w=o===x.value,v=x.disabled,k=o===m.value,R=m.disabled,z=(w?2:0)+(v?0:1),S=(k?2:0)+(R?0:1),y={[`${t}-radio-group__splitor--disabled`]:v,[`${t}-radio-group__splitor--checked`]:w},r={[`${t}-radio-group__splitor--disabled`]:R,[`${t}-radio-group__splitor--checked`]:k},s=z<S?r:y;n.push(p("div",{class:[`${t}-radio-group__splitor`,s]}),h)}}return{children:n,isButtonGroup:c}}const ge=Object.assign(Object.assign({},D.props),{name:String,value:[String,Number,Boolean],defaultValue:{type:[String,Number,Boolean],default:null},size:String,disabled:{type:Boolean,default:void 0},"onUpdate:value":[Function,Array],onUpdateValue:[Function,Array]}),ze=H({name:"RadioGroup",props:ge,setup(e){const o=_(null),{mergedSizeRef:t,mergedDisabledRef:i,nTriggerFormChange:n,nTriggerFormInput:c,nTriggerFormBlur:b,nTriggerFormFocus:h}=M(e),{mergedClsPrefixRef:a,inlineThemeDisabled:m,mergedRtlRef:x}=N(e),w=D("Radio","-radio-group",fe,Y,e,a),v=_(e.defaultValue),k=j(e,"value"),R=q(k,v);function z(l){const{onUpdateValue:f,"onUpdate:value":$}=e;f&&I(f,l),$&&I($,l),v.value=l,n(),c()}function S(l){const{value:f}=o;f&&(f.contains(l.relatedTarget)||h())}function y(l){const{value:f}=o;f&&(f.contains(l.relatedTarget)||b())}ue(J,{mergedClsPrefixRef:a,nameRef:j(e,"name"),valueRef:R,disabledRef:i,mergedSizeRef:t,doUpdateValue:z});const r=L("Radio",x,a),s=V(()=>{const{value:l}=t,{common:{cubicBezierEaseInOut:f},self:{buttonBorderColor:$,buttonBorderColorActive:P,buttonBorderRadius:T,buttonBoxShadow:U,buttonBoxShadowFocus:E,buttonBoxShadowHover:X,buttonColor:Z,buttonColorActive:ee,buttonTextColor:oe,buttonTextColorActive:te,buttonTextColorHover:re,opacityDisabled:ne,[F("buttonHeight",l)]:ae,[F("fontSize",l)]:ie}}=w.value;return{"--n-font-size":ie,"--n-bezier":f,"--n-button-border-color":$,"--n-button-border-color-active":P,"--n-button-border-radius":T,"--n-button-box-shadow":U,"--n-button-box-shadow-focus":E,"--n-button-box-shadow-hover":X,"--n-button-color":Z,"--n-button-color-active":ee,"--n-button-text-color":oe,"--n-button-text-color-hover":re,"--n-button-text-color-active":te,"--n-height":ae,"--n-opacity-disabled":ne}}),u=m?W("radio-group",V(()=>t.value[0]),s,e):void 0;return{selfElRef:o,rtlEnabled:r,mergedClsPrefix:a,mergedValue:R,handleFocusout:y,handleFocusin:S,cssVars:m?void 0:s,themeClass:u==null?void 0:u.themeClass,onRender:u==null?void 0:u.onRender}},render(){var e;const{mergedValue:o,mergedClsPrefix:t,handleFocusin:i,handleFocusout:n}=this,{children:c,isButtonGroup:b}=ve(se(ce(this)),o,t);return(e=this.onRender)===null||e===void 0||e.call(this),p("div",{onFocusin:i,onFocusout:n,ref:"selfElRef",class:[`${t}-radio-group`,this.rtlEnabled&&`${t}-radio-group--rtl`,this.themeClass,b&&`${t}-radio-group--button-group`],style:this.cssVars},c)}});export{Ce as NRadio,ke as NRadioButton,ze as NRadioGroup,we as radioButtonProps,ge as radioGroupProps,he as radioProps};
