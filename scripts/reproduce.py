"""Reproduce transparent summaries from Day 24 classroom archive.
Standard-library only; no network, no secret access or web scraping.
Usage: python reproduce.py <path-to-day24-zip> [output-json-path]
All figures are derived from supplied classroom datasets. They are NOT independently verified real-world claims.
"""
import csv,io,zipfile,json,hashlib,sys,collections,statistics,datetime
from pathlib import Path
PATHS={
'exams':'day20数据可视化进阶：考研数据图表绘制/02课程代码/各院校历年数据采集.csv',
'jobs':'day21未来职业规划行业薪资分析/02课程代码/兼职岗位数据.csv',
'social':'day14浏览器自动化社交平台数据精准抓取(1)/02课堂代码/小红书数据/小红书帖子.csv'
}
def median(l):return round(statistics.median(l),1) if l else None
def mean(l):return round(statistics.mean(l),1) if l else None
def main(archive,output):
  with zipfile.ZipFile(archive) as z:
    records={}; meta={}
    for k,suffix in PATHS.items():
      found=[i for i in z.namelist() if i.endswith(suffix)]
      if len(found)!=1:raise RuntimeError(f'Expected exactly one {k} source, found {len(found)}')
      raw=z.read(found[0]);rows=list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))); records[k]=rows
      meta[k]={'name':suffix,'sha256':hashlib.sha256(raw).hexdigest(),'source_rows':len(rows),'columns':len(rows[0])}
  e=records['exams']; years=sorted(set(r['录取年份'] for r in e)); schools=sorted(set(r['学校'] for r in e))
  erows=[]
  for y in years:
    for s in schools:
      group=[float(r['总分']) for r in e if r['录取年份']==y and r['学校']==s and r['总分']]
      if group:erows.append({'year':y,'school':s,'n':len(group),'mean':mean(group),'median':median(group),'min':min(group),'max':max(group)})
  school_counts=collections.Counter(r['学校'] for r in e);year_counts=collections.Counter(r['录取年份'] for r in e)
  exams={'rows':len(e),'distinct_rows':len({tuple(r.values()) for r in e}),'duplicate_rows':len(e)-len({tuple(r.values()) for r in e}),'schools':len(schools),'majors':len(set(r['专业'] for r in e)),'years':years,'year_counts':dict(sorted(year_counts.items())),'school_counts':dict(school_counts),'school_year':erows,'mean_total':mean([float(r['总分']) for r in e]),'median_total':median([float(r['总分']) for r in e]),'note':'课堂样本，未经官方高校网站核验；各校专业、口径不同，不可据此直接判断招生难度。'}
  j=records['jobs'];skills=sorted(set(r['技能方向'] for r in j)); cities=sorted(set(r['城市'] for r in j));
  skill_rows=[]
  for k in skills:
    group=[r for r in j if r['技能方向']==k];pay=[float(r['时薪_元']) for r in group];monthly=[float(r['预计月收入_元']) for r in group]
    skill_rows.append({'skill':k,'n':len(group),'mean_hourly':mean(pay),'median_hourly':median(pay),'mean_monthly':mean(monthly),'remote_pct':round(100*sum(r['远程办公']=='是' for r in group)/len(group),1)})
  city_rows=[]
  for city in cities:
    group=[r for r in j if r['城市']==city]; pay=[float(r['时薪_元']) for r in group]
    city_rows.append({'city':city,'n':len(group),'mean_hourly':mean(pay),'median_hourly':median(pay)})
  months=sorted(set(r['年月'] for r in j)); monthly=[]
  for m in months:
    group=[float(r['时薪_元']) for r in j if r['年月']==m]
    monthly.append({'month':m,'n':len(group),'mean_hourly':mean(group)})
  jobs={'rows':len(j),'cities':len(cities),'skills':skill_rows,'city_rows':city_rows,'months':monthly,'synthetic_rows':sum('模拟' in r['数据性质'] for r in j),'data_nature':sorted(set(r['数据性质'] for r in j)), 'note':'100% 为原始课件标注的模拟演示数据，不能代表实际招聘报价。'}
  social=records['social'];metrics=['点赞','收藏','评论','分享'];
  sm={'rows':len(social),'category_counts':dict(collections.Counter(r['类别'] for r in social)),'metrics':{},'note':'课堂采集快照；统计仅供学习，不公开昵称、帖文、链接或访问 token。'}
  for k in metrics:
    nums=[]
    for r in social:
      v=str(r[k]).strip().replace(',','')
      try:nums.append(int(float(v)))
      except (ValueError,TypeError):pass
    sm['metrics'][k]={'valid':len(nums),'total':sum(nums),'median':median(nums),'mean':mean(nums),'zero':sum(x==0 for x in nums),'max':max(nums)}
  report={'schema':'portfolio-results-v1','generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),'method':'Independent Python standard-library verification of supplied classroom CSV files. No network calls.','sources':meta,'exams':exams,'jobs':jobs,'social':sm}
  Path(output).parent.mkdir(parents=True,exist_ok=True)
  Path(output).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
  print(json.dumps({'sources':meta,'exams_summary':{k:v for k,v in exams.items() if k not in ('school_year','school_counts')},'jobs_summary':{k:v for k,v in jobs.items() if k not in ('city_rows','months','skills')},'social_summary':sm,'skills':skill_rows,'years':erows[:6]},ensure_ascii=False,indent=2))
if __name__=='__main__':
 if len(sys.argv)<2:raise SystemExit('Usage: python reproduce.py <zip> [output]')
 main(sys.argv[1],sys.argv[2] if len(sys.argv)>2 else 'data/results.json')
