import{N as A,i as J}from"./Input-CBFtFwWG.js";import{b as t,r as e,g as n,u as g,a0 as L,x as B,i as c,o as u,j as G,a1 as $}from"./bootstrap-Cg7-XUCZ.js";import{d as h,h as l,c as m}from"../jse/index-index-C-XMneWz.js";import"./use-locale-Db9MCNcL.js";import"./use-merged-state-Bwrns1mu.js";import"./Suffix-DGl6IH6C.js";import"./Eye-DjdBt23_.js";const k=t("input-group",`
 display: inline-flex;
 width: 100%;
 flex-wrap: nowrap;
 vertical-align: bottom;
`,[e(">",[t("input",[e("&:not(:last-child)",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `),e("&:not(:first-child)",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 margin-left: -1px!important;
 `)]),t("button",[e("&:not(:last-child)",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `,[n("state-border, border",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `)]),e("&:not(:first-child)",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `,[n("state-border, border",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `)])]),e("*",[e("&:not(:last-child)",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `,[e(">",[t("input",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `),t("base-selection",[t("base-selection-label",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `),t("base-selection-tags",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `),n("box-shadow, border, state-border",`
 border-top-right-radius: 0!important;
 border-bottom-right-radius: 0!important;
 `)])])]),e("&:not(:first-child)",`
 margin-left: -1px!important;
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `,[e(">",[t("input",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `),t("base-selection",[t("base-selection-label",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `),t("base-selection-tags",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `),n("box-shadow, border, state-border",`
 border-top-left-radius: 0!important;
 border-bottom-left-radius: 0!important;
 `)])])])])])]),S={},D=h({name:"InputGroup",props:S,setup(r){const{mergedClsPrefixRef:o}=g(r);return L("-input-group",k,o),{mergedClsPrefix:o}},render(){const{mergedClsPrefix:r}=this;return l("div",{class:`${r}-input-group`},this.$slots)}}),_=t("input-group-label",`
 position: relative;
 user-select: none;
 -webkit-user-select: none;
 box-sizing: border-box;
 padding: 0 12px;
 display: inline-block;
 border-radius: var(--n-border-radius);
 background-color: var(--n-group-label-color);
 color: var(--n-group-label-text-color);
 font-size: var(--n-font-size);
 line-height: var(--n-height);
 height: var(--n-height);
 flex-shrink: 0;
 white-space: nowrap;
 transition: 
 color .3s var(--n-bezier),
 background-color .3s var(--n-bezier),
 box-shadow .3s var(--n-bezier);
`,[n("border",`
 position: absolute;
 left: 0;
 right: 0;
 top: 0;
 bottom: 0;
 border-radius: inherit;
 border: var(--n-group-label-border);
 transition: border-color .3s var(--n-bezier);
 `)]),N=Object.assign(Object.assign({},c.props),{size:String,bordered:{type:Boolean,default:void 0}}),F=h({name:"InputGroupLabel",props:N,setup(r){const{mergedBorderedRef:o,mergedClsPrefixRef:i,inlineThemeDisabled:a}=g(r),f=B(r),{mergedSizeRef:p}=f,v=c("Input","-input-group-label",_,$,r,i),b=m(()=>{const{value:d}=p,{common:{cubicBezierEaseInOut:x},self:{groupLabelColor:z,borderRadius:C,groupLabelTextColor:I,lineHeight:R,groupLabelBorder:w,[u("fontSize",d)]:P,[u("height",d)]:y}}=v.value;return{"--n-bezier":x,"--n-group-label-color":z,"--n-group-label-border":w,"--n-border-radius":C,"--n-group-label-text-color":I,"--n-font-size":P,"--n-line-height":R,"--n-height":y}}),s=a?G("input-group-label",m(()=>{const{value:d}=p;return d[0]}),b,r):void 0;return{mergedClsPrefix:i,mergedBordered:o,cssVars:a?void 0:b,themeClass:s==null?void 0:s.themeClass,onRender:s==null?void 0:s.onRender}},render(){var r,o,i;const{mergedClsPrefix:a}=this;return(r=this.onRender)===null||r===void 0||r.call(this),l("div",{class:[`${a}-input-group-label`,this.themeClass],style:this.cssVars},(i=(o=this.$slots).default)===null||i===void 0?void 0:i.call(o),this.mergedBordered?l("div",{class:`${a}-input-group-label__border`}):null)}});export{A as NInput,D as NInputGroup,F as NInputGroupLabel,N as inputGroupLabelProps,S as inputGroupProps,J as inputProps};
