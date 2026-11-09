(()=>{'use strict';
const DATA=window.PORTFOLIO_DATA;
if(!DATA) return;
const qs=(s,root=document)=>root.querySelector(s);
const esc=(s)=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const catColors={'采集与分析':'violet','可视化':'blue','桌面应用':'orange','自动化':'teal'};
const sym={housing:'⌂',freelance:'≡',csvlab:'▥',exams:'⌁',desktop:'⌘',automation:'〈〉'};
const formatLink=(url)=>encodeURI(url).replace(/#/g,'%23');
const count=DATA.days.reduce((s,d)=>s+d.sources.length,0);
const codeCount=qs('#code-count');if(codeCount)codeCount.innerHTML=`${count}<span class="stat-small">FILES</span>`;
const prof=qs('#profile-name');if(prof)prof.textContent=DATA.profile.name;
const github=qs('#github-profile');if(github&&DATA.profile.githubUsername){github.href='https://github.com/'+encodeURIComponent(DATA.profile.githubUsername);github.classList.remove('hidden');}
const toggle=qs('#menu-toggle');if(toggle)toggle.addEventListener('click',()=>{const nav=qs('.nav-links');if(!nav)return;const active=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(active));});
const card=(p,i)=>`<a class="project-card ${catColors[p.category]||'blue'}" href="project.html?id=${encodeURIComponent(p.id)}" aria-label="查看项目：${esc(p.title)}"><div class="project-art"><div class="art-grid"></div><span class="project-art-symbol">${sym[p.id]||'▥'}</span><span class="art-tag">${esc(p.english)}</span><span class="art-index">0${i+1} / 06</span></div><div class="project-info"><div class="project-meta"><span>${esc(p.category)}</span><span>DAY ${esc(p.day)}</span></div><h3>${esc(p.title)}</h3><p>${esc(p.intro)}</p><div class="project-footer"><span class="label-light">${esc(p.status)}</span><span class="project-arrow">↗</span></div></div></a>`;
if(document.body.dataset.page==='home'){
 const grid=qs('#project-grid');const render=(category='全部')=>{const filtered=DATA.projects.filter(p=>category==='全部'||p.category===category);grid.innerHTML=filtered.map(card).join('')||'<p class="empty-state">该类别暂无项目。</p>';};
 render();qs('#project-filters').addEventListener('click',(ev)=>{const b=ev.target.closest('[data-category]');if(!b)return;qs('#project-filters').querySelectorAll('button').forEach(x=>x.classList.toggle('active',x===b));render(b.dataset.category);});
}
if(document.body.dataset.page==='project'){
 const id=new URLSearchParams(location.search).get('id');const p=DATA.projects.find(x=>x.id===id);
 const target=qs('#project-content');if(!p){target.innerHTML='<h1>没有找到对应项目</h1><p>请从精选项目列表重新选择。</p>';return;}
 document.title=p.title+' — Keji Portfolio';
 const links=p.links.map(([label,path])=>`<a class="resource-link" target="_blank" rel="noopener noreferrer" href="${formatLink(path)}"><span>${esc(label)}</span><span>↗</span></a>`).join('');
 target.innerHTML=`<div class="detail-hero"><div><p class="kicker">${esc(p.english)} / DAY ${esc(p.day)}</p><h1>${esc(p.title)}</h1><p class="detail-intro">${esc(p.intro)}</p><div class="skill-chips">${p.skills.map(s=>`<span>${esc(s)}</span>`).join('')}</div><div class="detail-badges"><span>${esc(p.category)}</span><span>${esc(p.status)}</span></div></div><div class="detail-art ${catColors[p.category]||'blue'}"><span class="detail-glyph">${sym[p.id]||'⌘'}</span><div class="detail-art-copy">COURSE TO PORTFOLIO<br><strong>${esc(p.english)}</strong></div></div></div>
 <div class="detail-columns"><div class="detail-main"><article class="detail-section"><p class="section-number">01 / CONTEXT</p><h2>为什么做这个项目</h2><p>${esc(p.context)}</p></article><article class="detail-section"><p class="section-number">02 / PROCESS</p><h2>实现过程</h2><ol class="process-list">${p.process.map((x,i)=>`<li><span>0${i+1}</span>${esc(x)}</li>`).join('')}</ol></article><article class="detail-section"><p class="section-number">03 / RESULT</p><h2>学习成果</h2><p>${esc(p.output)}</p>${p.demo?`<a class="btn btn-primary detail-demo" href="${formatLink(p.demo)}">打开交互演示 <span>↗</span></a>`:''}</article></div><aside class="detail-aside"><p class="kicker">SOURCE & NOTES</p><h3>相关代码与资源</h3>${links||'<p>本阶段暂无公开示例代码。</p>'}<div class="source-note">${esc(p.note)}</div></aside></div>`;
}
if(document.body.dataset.page==='knowledge'){
 const list=qs('#archive-list');const search=qs('#search-days');const sel=qs('#category-days');
 const urlDay=parseInt(new URLSearchParams(location.search).get('day'),10);
 function render(){const q=search.value.trim().toLowerCase(),category=sel.value;let filtered=DATA.days.filter(d=>(category==='全部'||d.category===category)&&(!q||('day '+d.day+' '+d.title+' '+d.topics+' '+d.summary+' '+d.category).toLowerCase().includes(q)));
 qs('#archive-count').textContent=`显示 ${filtered.length} / 24 个学习单元`;
 list.innerHTML=filtered.map(d=>`<details class="archive-card" ${d.day===urlDay?'open':''} id="day${d.day}"><summary><span class="archive-day">${String(d.day).padStart(2,'0')}</span><span class="archive-title"><strong>${esc(d.title)}</strong><small>${esc(d.topics)}</small></span><span class="archive-tag">${esc(d.category)}</span><span class="archive-expand">＋</span></summary><div class="archive-content"><p>${esc(d.summary)}</p><div class="archive-code-head">${esc(d.kind)} · ${d.sources.length} 份可查看文件</div><div class="archive-links">${d.sources.length?d.sources.map(p=>`<a href="${formatLink(p)}" target="_blank" rel="noopener noreferrer">${esc(p.split('/').at(-1))} ↗</a>`).join(''):'<span class="archive-none">本次公开包未收录该天的源代码；保留课程主题与知识点。</span>'}</div></div></details>`).join('')||'<p class="empty-state">没有匹配的课程，请调整搜索条件。</p>';
 }
 search.addEventListener('input',render);sel.addEventListener('change',render);render();
 if(Number.isFinite(urlDay)&&urlDay>0){const el=qs('#day'+urlDay);if(el)setTimeout(()=>el.scrollIntoView({block:'center'}),80);}
}
})();
