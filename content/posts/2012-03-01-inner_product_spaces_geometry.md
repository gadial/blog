---
id: 1522
title: "(קצת על) הגאומטריה של מרחבי מכפלה פנימית"
date: 2012-03-01 20:08:19
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - אלגברה לינארית
  - גאומטריה
  - מרחבי מכפלה פנימית
---
בפוסט הקודם על אלגברה לינארית הצגנו את מושג המכפלה הפנימית וכמה מושגים נלווים, אבל לא דיברנו על מה שלדעתי הוא הדבר העיקרי פה - האופן שבו מכפלה פנימית משרה על מרחבים וקטורים <strong>גאומטריה</strong>, במובן זה שאם יש לנו מכפלה פנימית על מרחב יש לנו מושגים של אורך וזווית ודברים שנובעים מהם.

נתחיל עם היצור שהגדרתי בפוסט הקודם כחלק אגבי מתהליך גרם-שמידט: נורמה. כזכור, אם {% equation %}x\in V{% endequation %} אז הגדרתי {% equation %}\|x\|=\sqrt{\left\langle x,x\right\rangle }{% endequation %}, בהתבסס על כך ש-{% equation %}\left\langle x,x\right\rangle {% endequation %} הוא מספר ממשי חיובי (והפונקציה {% equation %}\sqrt{}{% endequation %}, כתמיד, מחזירה את השורש החיובי). הנורמה מקיימת שלוש תכונות שמאפיינות כל כך טוב את מושג ה"אורך" שאפשר לראות אותה כהכללה טבעית שלו:
<ol>
	<li> {% equation %}\|x\|\ge0{% endequation %} ו-{% equation %}\|x\|=0{% endequation %} אם ורק אם {% equation %}x=0{% endequation %}.</li>
	<li> {% equation %}\|\lambda x\|=\left|\lambda\right|\|x\|{% endequation %} לכל סקלר {% equation %}\lambda\in\mathbb{F}{% endequation %}</li>
	<li> {% equation %}\|x+y\|\le\|x\|+\|y\|{% endequation %} ("אי שוויון המשולש").</li>
</ol>
תכונה 1 היא פשוט דרישה 4 בהגדרת מכפלה פנימית.

תכונה 2 נובעת מתכונות 2 ו-3 של מכפלה פנימית: {% equation %}\|\lambda x\|^{2}=\left\langle \lambda x,\lambda x\right\rangle =\lambda\overline{\lambda}\left\langle x,x\right\rangle =\left|\lambda\right|^{2}\|x\|^{2}{% endequation %} ולכן על ידי הוצאת שורש נקבל את התכונה.

תכונה 3 לעומת זאת היא מעניינת ולא מיידית. השם "אי שוויון המשולש" נובע מכך שבמשולש, סכום אורכי כל שתי צלעות הוא תמיד גדול מאורך הצלע השלישית. עוד מעט נראה שהתכונה הזו היא המהותית ביותר כאשר אנחנו רוצים לדבר על <strong>מרחק</strong>, שכן היא מונעת סיטואציה אבסורדית שבה מרחק בין שתי נקודות <strong>גדול</strong> מהמרחק בין שתיהן לאיזו נקודה בצד (ולכן יותר מהיר ללכת לא מהנקודה הראשונה לשניה אלא לעבור קודם בנקודה הצדדית). את תכונה 3 אי אפשר להרוויח "סתם" - נשתמש בטענת עזר שהיא חשובה ביותר בזכות עצמה.

ראשית, בואו ננסה להוכיח את הטענה פשוט מההגדרות:

{% equation %}\|x+y\|^{2}=\left\langle x+y,x+y\right\rangle =\left\langle x,x\right\rangle +\left\langle x,y\right\rangle +\left\langle y,x\right\rangle +\left\langle y,y\right\rangle {% endequation %}

{% equation %}=\|x\|^{2}+\left\langle x,y\right\rangle +\overline{\left\langle x,y\right\rangle }+\|y\|^{2}=\|x\|^{2}+2\mbox{Re}\left\langle x,y\right\rangle +\|y\|^{2}{% endequation %}

המממפף. כאן אנחנו נתקעים, כי לא ברור לנו מה לעשות עם ה-{% equation %}2\mbox{Re}\left\langle x,y\right\rangle {% endequation %} שתקוע לנו כאן. אנחנו רוצים להבין משהו על טיב הקשר שבין {% equation %}\left\langle x,y\right\rangle {% endequation %} ו-{% equation %}\|x\|,\|y\|{% endequation %}. לצורך כך, בואו ניזכר במכפלות סקלריות: הגדרנו מכפלה סקלרית ב-{% equation %}\mathbb{R}^{2}{% endequation %} בתור מכפלת ה<strong>אורכים</strong> של וקטורים בקוסינוס הזווית ביניהם. במילים אחרות, המכפלה הסקלרית הייתה <strong>לכל היותר</strong> מכפלת האורכים של הוקטורים; לרוב היא "התקזזה" קצת בגלל שהוקטורים לא הצביעו לאותו הכיוון. את התחושה האינטואיטיבית הזו אפשר לתרגם לאי-שוויון קונקרטי:

{% equation %}\left|\left\langle x,y\right\rangle \right|\le\|x\|\|y\|{% endequation %}

לאי השוויון הזה קוראים <strong>אי שוויון קושי-שוורץ</strong>, והוא אחד מאותם משפטים מתמטיים שבהם אני נתקל <strong>בכל מקום</strong> (לעתים קרובות בניסוח למקרה פרטי עבור מכפלה פנימית ספציפית, ואז הוא נראה מסורבל <strong>יותר</strong> וקשה יותר להבנה). קשה להפריז בחשיבות שלו, אבל למרבה המזל ההוכחה שלו אינו קשה במיוחד. לפני שנוכיח אותו בואו נראה איך הוא מסיים עם אי-שוויון המשולש: {% equation %}2\mbox{Re}\left\langle x,y\right\rangle \le2\left|\left\langle x,y\right\rangle \right|\le2\|x\|\|y\|{% endequation %} ולכן:

{% equation %}\|x+y\|^{2}\le\|x\|^{2}+2\|x\|\|y\|+\|y\|^{2}=\left(\|x\|+\|y\|\right)^{2}{% endequation %}

ועל ידי הוצאת שורש משני האגפים מקבלים את אי-שוויון המשולש.

יופי, אז איך מוכיחים את קושי-שוורץ? גם כאן כדאי לזכור את מה שהלך עם מכפלה סקלרית. בדוגמה שנתתי, עם עבודה של כוח על גוף, לקחנו את הוקטור שתיאר את העבודה ופירקנו אותו לשני רכיבים - אחד בכיוון תנועת הגוף, והשני בניצב לכיוון הזה. המכפלה הסקלרית של הרכיב הראשון עם הכיוון הייתה בדיוק מכפלה של שני גדלי הוקטורים; המכפלה הסלקרית של הרכיב השני עם הכיוון הייתה 0 (כי הם ניצבים). זה גם מה שנעשה כאן, ונשתמש בדיוק באותם רעיונות שבהם השתמשנו בתהליך גרם-שמידט. ראשית ניקח את {% equation %}x{% endequation %} וננרמל אותו - נגדיר {% equation %}a=\frac{x}{\|x\|}{% endequation %} (כאן עלינו להניח ש-{% equation %}x\ne0{% endequation %} אבל אם {% equation %}x=0{% endequation %} אז {% equation %}\left\langle x,y\right\rangle =0=\|0\|\|y\|{% endequation %} ואי השוויון טריוויאלי). כעת נגדיר {% equation %}b=y-\left\langle y,a\right\rangle a{% endequation %} . כלומר, {% equation %}b{% endequation %} הוא בדיוק מה שנשאר מ-{% equation %}y{% endequation %} אחרי שמחסרים ההטלה של {% equation %}y{% endequation %} על וקטור היחידה {% equation %}a{% endequation %} שנמצא באותו כיוון כמו {% equation %}x{% endequation %}. בפרט, {% equation %}\left\langle b,a\right\rangle =0{% endequation %}

כעת:

{% equation %}0\le\|b\|^{2}=\left\langle b,b\right\rangle =\left\langle b,y-\left\langle y,a\right\rangle a\right\rangle {% endequation %}

{% equation %}=\left\langle b,y\right\rangle -\left\langle b,\left\langle y,a\right\rangle a\right\rangle =\left\langle b,y\right\rangle {% endequation %}

{% equation %}=\left\langle y-\left\langle y,a\right\rangle a,y\right\rangle =\left\langle y,y\right\rangle -\left\langle y,a\right\rangle \left\langle a,y\right\rangle {% endequation %}

{% equation %}=\|y\|^{2}-\frac{\left\langle y,x\right\rangle \left\langle x,y\right\rangle }{\|x\|^{2}}=\|y\|^{2}-\frac{\left|\left\langle x,y\right\rangle \right|^{2}}{\|x\|^{2}}{% endequation %}

העברת אגפים, כפל, הוצאת שורש וקיבלנו {% equation %}\left|\left\langle x,y\right\rangle \right|\le\|x\|\|y\|{% endequation %}. החישוב שלמעלה נראה טיפה טכני אבל הוא מיידי למדי, והעיקר פה הוא הרעיון שהצגתי קודם.

בואו ננצל את ההזדמנות הזו ונציג רעיון שלא אשתמש בו בהמשך אבל שווה לשים אליו לב: מכיוון ש-{% equation %}\left|\left\langle x,y\right\rangle \right|\le\|x\|\|y\|{% endequation %} הרי ש-{% equation %}0\le\frac{\left|\left\langle x,y\right\rangle \right|}{\|x\|\|y\|}\le1{% endequation %} תמיד ולכן אפשר לדבר על {% equation %}\mbox{arccos}\left(\frac{\left|\left\langle x,y\right\rangle \right|}{\|x\|\|y\|}\right){% endequation %} - הביטוי הזה ייתן לנו לנו זווית בין 0 ל-90 מעלות, שבמובן מסויים ניתן לחשוב עליה בתור הזווית בין {% equation %}x{% endequation %} ו-{% equation %}y{% endequation %}. בפרט, אם {% equation %}\left\langle x,y\right\rangle =0{% endequation %} אז הזווית היא בת 90 מעלות, בהתאם לרעיון שלנו של "וקטורים אורתוגונליים הם מאונכים". אבל כאמור, אני לא הולך להגיד על זה יותר שום דבר.

כעת, צריך להיזהר ולא לתת את הרושם השגוי שנורמות צצות רק בהקשרים של מכפלה פנימית. כל פונקציה {% equation %}V\to\mathbb{R}{% endequation %} עבור מרחב וקטורי {% equation %}V{% endequation %} שמקיימת את תכונות 1-3 היא נורמה (אפשר לדבר על נורמות גם בהקשרים שאינם של מרחבים וקטוריים, אבל צריך לתקן את התכונות בהתאם - בפרט תכונה 2), ו<strong>לא כל נורמה מתקבלת ממכפלה פנימית</strong>. כלומר, ייתכן שנגדיר נורמה על מרחב {% equation %}V{% endequation %} כך שפשוט אין מכפלה פנימית על {% equation %}V{% endequation %} שנותנת את הנורמה הזו. איך אפשר להוכיח דבר כזה? או, טוב ששאלתם. בואו נראה שלוש נורמות שונות על {% equation %}\mathbb{R}^{2}{% endequation %} - שלוש מה"פופולריות" ביותר:
<ol>
	<li> הנורמה האוקלידית הרגילה: {% equation %}\|\left(x,y\right)\|_{2}=\sqrt{x^{2}+y^{2}}{% endequation %}</li>
	<li> נורמת "נהגי המוניות": {% equation %}\|\left(x,y\right)\|_{1}=\left|x\right|+\left|y\right|{% endequation %}</li>
	<li> נורמת הסופרמום: {% equation %}\|\left(x,y\right)\|_{\infty}=\mbox{max}\left\{ \left|x\right|,\left|y\right|\right\} {% endequation %}</li>
</ol>
לא אוכיח שאלו נורמות אבל די קל לראות את זה (בפרט שתי התכונות הראשונות הן מיידיות). הסימונים הדומים עבור הנורמות הללו אינם מקריים: באופן כללי, לכל מספר ממשי {% equation %}p\ge1{% endequation %} אפשר להגדיר נורמה על ידי {% equation %}\|\left(x,y\right)\|_{p}=\left(\left|x\right|^{p}+\left|y\right|^{p}\right)^{\frac{1}{p}}{% endequation %} מה שמכליל לנו את שתי הנורמות הראשונות, והשלישית מתקבלת כאשר {% equation %}p\to\infty{% endequation %} (במובן שלא אכנס אליו כרגע).

ההמחשה הטובה ביותר לאופי של הנורמות הללו, לטעמי, היא הציור של "מעגל היחידה" בכל אחד מהן - אוסף כל הנקודות שהמרחק שלהן מהראשית הוא 1, כלומר הוקטור שמתחיל בראשית ונגמר בהן הוא מנורמה 1:

<strong><a href="{{site.baseurl}}{{site.post_images}}/2012/03/140px-Vector_norms.svg_.png"><img class="alignnone size-full wp-image-1524" title="140px-Vector_norms.svg" src="{{site.baseurl}}{{site.post_images}}/2012/03/140px-Vector_norms.svg_.png" alt="" width="140" height="460" /></a>
</strong>

למי שהאיור הזה נראה לו מופרך לגמרי - נסו זאת בעצמכם! נסו לחשוב כיצד לצייר את מעגלי היחידה עבור שתי הנורמות ה"חדשות". זה קל באופן מפתיע ואחרי זה המעגלים הללו לא ייראו מוזר כל כך.

כעת אני רוצה לטעון שיש תכונה שכל נורמה שמושרית ממכפלה פנימית חייבת לקיים - תכונה שהיא גאומטרית במהותה: <strong>כלל המקבילית</strong>. נניח שיש לנו שני וקטורים, {% equation %}a,b{% endequation %}. אפשר לחשוב עליהם כעל שתי צלעות של מקבילית. לא קשה לראות שהאלכסונים של אותה מקבילית יהיו {% equation %}a+b{% endequation %} ו-{% equation %}a-b{% endequation %}:

<strong><a href="{{site.baseurl}}{{site.post_images}}/2012/03/Parallelogram_law.png"><img class="alignnone size-full wp-image-1525" title="Parallelogram_law" src="{{site.baseurl}}{{site.post_images}}/2012/03/Parallelogram_law.png" alt="" width="311" height="414" /></a></strong>

כעת, כלל המקבילית הוא מין הכללה של משפט פיתגורס: סכום ריבועי אורכי כל צלעות המקבילית שווה לסכום ריבועי אורכי האלכסונים. בלשון נורמות:

{% equation %}2\|a\|^{2}+2\|b\|^{2}=\|a+b\|^{2}+\|a-b\|^{2}{% endequation %}

למה הכללה של פיתגורס? כי אם {% equation %}a,b{% endequation %} מאונכים זה לזה המקבילית היא מלבן, והאלכסונים בה שווים, ולכן על ידי חלוקה ב-2 מקבלים בדיוק {% equation %}\|a\|^{2}+\|b\|^{2}=\|a+b\|^{2}{% endequation %}; אבל היופי בכלל המקבילית הוא שהוא נכון תמיד, בכל מקבילית.

איך מוכיחים את זה? אפשר עם גאומטריה אוקלידית, אבל אני רוצה לתת כאן הוכחה שתעבוד בכל מרחב מכפלה פנימית שהוא. ובכן, בואו פשוט ננסה לעבוד עם ההגדרה:

{% equation %}\|a+b\|^{2}+\|a-b\|^{2}=\left\langle a+b,a+b\right\rangle +\left\langle a-b,a-b\right\rangle {% endequation %}

{% equation %}=\left(\left\langle a,a\right\rangle +\left\langle a,b\right\rangle +\left\langle b,a\right\rangle +\left\langle b,b\right\rangle \right)+\left(\left\langle a,a\right\rangle -\left\langle a,b\right\rangle -\left\langle b,a\right\rangle +\left\langle b,b\right\rangle \right){% endequation %}

{% equation %}=2\left\langle a,a\right\rangle +2\left\langle b,b\right\rangle =2\|a\|^{2}+2\|b\|^{2}{% endequation %}

וואו. זה היה... קל. די מפתיע איך דרך ההצגה הזו של נורמות ומכפלות פנימיות הופכת דברים מסויימים לטריוויאליים.

ובכן, בואו נראה מה מעוללת נורמת הסופרמום בהקשר של כלל המקבילית, עם הוקטורים {% equation %}a=\left(1,0\right){% endequation %} ו-{% equation %}b=\left(0,1\right){% endequation %}:

{% equation %}2\|\left(1,0\right)\|_{\infty}^{2}+2\|\left(0,1\right)\|_{\infty}^{2}=2+2=4{% endequation %}

{% equation %}\|\left(1,1\right)\|_{\infty}^{2}+\|\left(1,-1\right)\|_{\infty}^{2}=1+1=2{% endequation %}

אופס! כלל המקבילית לא מתקיים! לכן אנו רואים, מייד, שנורמת הסופרמום לא נתקבלה ממכפלה פנימית.

ומה על נורמת נהגי המוניות? ובכן, {% equation %}\left(1,0\right),\left(0,1\right){% endequation %} דווקא לא יגרמו צרות, אבל:

{% equation %}2\|\left(2,0\right)\|_{1}^{2}+2\|\left(0,2\right)\|_{1}^{2}=8+8=16{% endequation %}

{% equation %}\|\left(2,2\right)\|_{1}^{2}+\|\left(2,-2\right)\|_{1}^{2}=16+16=32{% endequation %}

ולכן גם נורמת נהגי המוניות לא מתקבלת ממכפלה פנימית. מצאנו קריטריון פשוט ונחמד לבדוק מתי נורמה לא מושרית ממכפלה פנימית, אבל מסתבר שהקריטריון עוד יותר חזק מכך: אם נורמה כלשהי <strong>כן</strong> מקיימת את כלל המקבילית, אז היא <strong>כן</strong> מושרית ממכפלה פנימית, ואפילו אפשר לייצג את המכפלה הפנימית בעזרת הנורמה. בואו נניח לרגע שאנחנו מעל {% equation %}\mathbb{R}{% endequation %} ושיש לנו נורמה {% equation %}\|\cdot\|{% endequation %} שמקיימת את כלל המקבילית, ונשחק ב"נדמה לי" שהנורמה אכן הושרתה על ידי מכפלה פנימית, כלומר {% equation %}\|x\|^{2}=\left\langle x,x\right\rangle {% endequation %}. כפי שכבר ראינו, {% equation %}\|a+b\|^{2}=\|a\|^{2}+\left\langle a,b\right\rangle +\left\langle b,a\right\rangle +\|b\|^{2}{% endequation %}, ואם אנחנו מעל {% equation %}\mathbb{R}{% endequation %} אז {% equation %}\left\langle a,b\right\rangle =\left\langle b,a\right\rangle {% endequation %}, ולכן קיבלנו:

{% equation %}\left\langle a,b\right\rangle =\frac{\|a+b\|^{2}-\|a\|^{2}-\|b\|^{2}}{2}{% endequation %}

כלומר, עלה בידינו להביע את המכפלה הפנימית של שני איברים שרירותיים באמצעות הנורמה בלבד.

את הביטוי למעלה אפשר לשנות קצת כדי לקבל משהו יותר סימטרי. אם נחזור על התעלול ונפתח את {% equation %}\|a-b\|^{2}{% endequation %} נקבל בסוף {% equation %}\left\langle a,b\right\rangle =\frac{\|a\|^{2}+\|b\|^{2}-\|a-b\|^{2}}{2}{% endequation %}. מחיבור שני הביטויים ל-{% equation %}\left\langle a,b\right\rangle {% endequation %} וחלוקה ב-2 נקבל:

{% equation %}\left\langle a,b\right\rangle =\frac{\|a+b\|^{2}-\|a-b\|^{2}}{4}{% endequation %}

זהות זו נקראת <strong>זהות הפולריזציה</strong>.

אם אנחנו מעל {% equation %}\mathbb{C}{% endequation %} אותו תעלול יעבוד אבל הנוסחה תהיה מסובכת יותר בגלל שכבר לא מתקיים ש-{% equation %}\left\langle a,b\right\rangle =\left\langle b,a\right\rangle {% endequation %}:

{% equation %}\left\langle a,b\right\rangle =\frac{\|x+y\|^{2}-\|x-y\|^{2}+i\|x+iy\|^{2}-i\|x-iy\|^{2}}{4}{% endequation %}

עכשיו אפשר לחזור ביתר שאת לדיון הגאומטרי. הסכמנו כבר (אני מקווה) שנורמה מייצגת "אורך". אם {% equation %}u,v{% endequation %} הם שני איברים במרחב {% equation %}V{% endequation %} אז {% equation %}u-v{% endequation %} הוא הוקטור המחבר ביניהן (ו-{% equation %}v-u{% endequation %} הוא אותו וקטור, בכיוון ההפוך). כלומר, {% equation %}\|u-v\|{% endequation %} הוא אורך הוקטור שמחבר את {% equation %}u{% endequation %} עם {% equation %}v{% endequation %}, דהיינו ה<strong>מרחק</strong> בין {% equation %}u{% endequation %} ו-{% equation %}v{% endequation %}. בלשון יותר פורמלית, כל נורמה משרה <strong>מטריקה</strong> - מטריקה היא הכללה של מושג המרחק כשם שנורמה היא הכללה של מושג האורך, אבל מטריקה היא מושג כללי יותר (אפשר להגדיר מטריקות גם על מרחבים שאינם וקטוריים ומרחבים שאין כל משמעות לדיבורים על נורמה בהם). לא אציג עכשיו את התורה של מרחבים מטריים; נסתפק בתחושה האינטואיטיבית ש-{% equation %}\|u-v\|{% endequation %} אכן מייצג מרחק ונראה מה עושים עם זה כאן.

אולי מוכרת לכם תוצאה מגאומטריה ב-{% equation %}\mathbb{R}^{2}{% endequation %}: אם נתון לנו ישר ונקודה מחוצה לו, אז מרחק הנקודה מהישר הוא אורך האנך מהנקודה לישר - כש"אנך" הוא קו שמועבר בין הנקודה אל עבר נקודה כלשהי על הישר, כך שהזווית שהוא יוצר עם הישר היא בת 90 מעלות. מה זה אומר שאורך האנך הוא ה"מרחק" של הנקודה מהישר? שאורכו הוא המרחק <strong>הקטן ביותר</strong> של הנקודה מכל נקודה על הישר.

אפשר לדבר על אותה סיטואציה גם במרחב מכפלה פנימית כללי (במקרה שלנו, סוף-ממדי. אנחנו תמיד מדברים על מרחבים סוף ממדיים בכל הסיפור הזה). אצלנו את מקום הנקודה תופס וקטור {% equation %}u{% endequation %}, ואת מקום הישר תופס תת-מרחב {% equation %}W\subseteq V{% endequation %}. וכעת הטענה היא: {% equation %}\min\left\{ \|u-w\||w\in W\right\} {% endequation %} קיים ומתקבל בנקודה <strong>יחידה</strong> {% equation %}w_{0}\in W{% endequation %}. כדי להבין למה לא טריוויאלי שמינימום על קבוצת מספרים יהיה תמיד קיים, הביטו בקבוצה {% equation %}\left\{ 1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\dots\right\} {% endequation %} שבבירור אין לה מינימום - האיברים בקבוצה "הולכים ומתקרבים" לאפס, אבל אפס אינו איבר בקבוצה (אפס הוא כן מה שנקרא <strong>האינפימום</strong> של הקבוצה, אבל לא על זה מדברים פה).

המקרה הדו-ממדי הפשוט נותן לנו אינטואיציה חזקה מאוד לגבי מה שצריך לעשות כאן: אנחנו מצפים שאם {% equation %}w_{0}{% endequation %} קיימת, אז הוקטור {% equation %}u-w_{0}{% endequation %} יהיה מאונך ל"ישר" {% equation %}W{% endequation %}, כלומר שיהיה אורתוגונלי לכל וקטור בתת-המרחב {% equation %}W{% endequation %}, כלומר שיתקיים {% equation %}\left\langle u-w_{0},w\right\rangle =0{% endequation %} לכל {% equation %}w\in W{% endequation %}. הבה ונתחיל מלהראות שאכן קיים {% equation %}w_{0}\in W{% endequation %} כך ש-{% equation %}u-w_{0}{% endequation %} אורתוגונלי לכל {% equation %}W{% endequation %}.

מכיוון ש-{% equation %}V{% endequation %} ממימד סופי כך גם {% equation %}W{% endequation %} ולכן קיים ל-{% equation %}W{% endequation %} בסיס אורתונורמלי (גרם-שמידט...) {% equation %}\left\{ e_{1},\dots,e_{k}\right\} {% endequation %}. כמו שכבר ראינו כשהתעסקנו עם גרם-שמידט, {% equation %}\sum\left\langle u,e_{i}\right\rangle e_{i}{% endequation %} הוא בדיוק הרכיב של {% equation %}u{% endequation %} שחי "בתוך" {% equation %}W{% endequation %} - ה<strong>הטלה</strong> של {% equation %}u{% endequation %} על {% equation %}W{% endequation %}. וכפי שראינו, {% equation %}u-\sum\left\langle u,e_{i}\right\rangle e_{i}{% endequation %} יהיה אורתוגונלי לכל אחד מוקטורי הבסיס {% equation %}e_{i}{% endequation %} ולכן אורתוגונלי לכל {% equation %}W{% endequation %}. כלומר, נגדיר {% equation %}w_{0}=\sum\left\langle u,e_{i}\right\rangle e_{i}{% endequation %}. אולי עכשיו קצת יותר ברור למה נכון לחשוב עליו כעל "הטלה" - הפיסות מתחילות להתחבר.

מה שהולך לקרות עכשיו תקף גם במרחבים שאינם סוף-ממדיים, בעצם: אני הולך להראות שאם {% equation %}u-w_{0}{% endequation %}אורתוגונלי לכל {% equation %}W{% endequation %} (כאשר {% equation %}w_{0}{% endequation %} וקטור כלשהו ב-{% equation %}W{% endequation %} ולא משנה איך הגעתי אליו - העיקר שתתקיים תכונת האורתוגונליות) אז {% equation %}\|u-w_{0}\|{% endequation %} אכן מינימלי. לצורך כך בואו ניקח {% equation %}w\in W{% endequation %} כלשהו השונה מ-{% equation %}w_{0}{% endequation %}, וננסה להעריך את {% equation %}\|u-w\|{% endequation %} תוך שימוש באחד התעלולים הכי סטנדרטיים באנליזה (וברגע שהתחלנו לדבר על נורמות, בין אם נרצה ובין אם לאו, אנחנו מתחילים להתעסק באנליזה) - להוסיף ולהחסיר את אותו איבר:

{% equation %}\|u-w\|^{2}=\|u-w_{0}+w_{0}-w\|^{2}=\|u-w_{0}\|^{2}+2\mbox{Re}\left\langle u-w_{0},w_{0}-w\right\rangle +\|w_{0}-w\|^{2}{% endequation %}

רק מה, {% equation %}w_{0}-w\in W{% endequation %} כי אנו מחסירים זה מזה שני איברים ב-{% equation %}W{% endequation %}, ולכן המכפלה הפנימית באמצע היא 0, ולכן קיבלנו ש-{% equation %}\|u-w\|^{2}{% endequation %} שווה ל-{% equation %}\|u-w_{0}\|^{2}{% endequation %} ועוד משהו חיובי, שהרי {% equation %}w_{0}\ne w{% endequation %} ולכן {% equation %}\|w_{0}-w\|^{2}{% endequation %} חייב להיות חיובי. סוף הסיפור - הראינו שאם {% equation %}u-w_{0}{% endequation %} אורתוגונלי ל-{% equation %}W{% endequation %} אז {% equation %}w_{0}{% endequation %} הוא "הקירוב הטוב ביותר" ל-{% equation %}u{% endequation %} ב-{% equation %}W{% endequation %}. אפשר להראות גם ההפך - שאם {% equation %}w_{0}{% endequation %} הוא הקירוב הטוב ביותר אז {% equation %}u-w_{0}{% endequation %} אורתוגונלי ל-{% equation %}W{% endequation %}; ההוכחה קצת יותר טכנית ולכן אתחמק ממנה.

צריך עדיין להראות שאם {% equation %}w_{0}{% endequation %} המהולל קיים הוא גם יחיד. כדי לחשוב על סיטואציה שבה קירוב טוב ביותר הוא לא יחיד, חשבו על קבוצה בצורת פרסה, ונקודה שנמצאת בדיוק באמצע הרווח שבין שני צדדי הפרסה. אלא שפרסה איננה תת-מימד ולכן לא רלוונטית למשפט שלנו (למעשה, אפשר לחזק את המשפט שלנו ולדרוש ש-{% equation %}W{% endequation %} תהיה רק קבוצה <strong>קמורה</strong>, אבל נעזוב את זה). ההוכחה כאן קצרה להפתיע, בהינתן ההוכחה של מה שחמקתי מלהוכיח פסקה קודם: אם שני וקטורים הם קירובים-טובים-ביותר, אז {% equation %}u{% endequation %} פחות כל אחד מהם אורתוגונלי לכל {% equation %}W{% endequation %}, ופשוט לא ייתכן שזה יתקיים עבור שני וקטורים שונים, כי שימו לב להוכחה שבה הראיתי שוקטור אורתוגונלי נותן את הקירוב הטוב ביותר - <strong>לכל</strong> וקטור אחר ב-{% equation %}W{% endequation %}, קיבלנו ש-{% equation %}\|u-w\|&gt;\|u-w_{0}\|{% endequation %}.

התוצאה הזו היא יפה בפני עצמה, אבל עדיין חסר העוקץ. לצורך כך, הבה ונוסיף הגדרה אחת אחרונה למשחק: אם {% equation %}W{% endequation %} הוא תת-מרחב של {% equation %}V{% endequation %}, נסמן ב-{% equation %}W^{\perp}{% endequation %} את <strong>המשלים האורתוגונלי</strong> שלו - המשמעות של השם תכף תתברר, אבל בינתיים נסתפק בהגדרה היבשה של "כל הוקטורים ב-{% equation %}V{% endequation %} שאורתוגונליים לכל הוקטורים ב-{% equation %}W{% endequation %}", כלומר {% equation %}W^{\perp}=\left\{ v\in V|\forall w\in W:\left\langle v,w\right\rangle =0\right\} {% endequation %}.

הבה ונסמן ב-{% equation %}E{% endequation %} את הפונקציה שבהינתן וקטור {% equation %}u{% endequation %} מחזירה את ההיטל שלו ב-{% equation %}W{% endequation %}. זוהי טרנספורמציה לינארית, כפי שניתן לראות מהמשוואה שהגדירה את {% equation %}w_{0}{% endequation %} ותכונות הלינאריות של מכפלה פנימית. יותר מכך, זוהי <strong>הטלה</strong> במובן שהגדרתי לפני אי-אילו פוסטים, כלומר מתקיים {% equation %}E^{2}=E{% endequation %} כי {% equation %}E\left(w\right)=w{% endequation %} לכל {% equation %}w\in W{% endequation %} (למה? זה באמת לא קשה). אם אתם זוכרים במעורפל, בשעתו השתמשנו בהטלות כדי לפרק את המרחב כולו לסכום ישר של תתי-המרחבים שעליהם ההטלות, ובכן, מטילות. גם כאן אני טוען שמתקיים {% equation %}V=W\oplus W^{\perp}{% endequation %}, לכל {% equation %}W{% endequation %}. איך נראה את זה?

ניקח {% equation %}v\in V{% endequation %} כלשהו. אז {% equation %}Ev\in W{% endequation %} על פי ההגדרה. מכאן שאפשר לכתוב {% equation %}v=Ev+\left(v-Ev\right){% endequation %}, וכפי שאמרתי קודם (אבל חמקתי מלהוכיח), {% equation %}v-Ev\in W^{\perp}{% endequation %}. צריך גם לראות ש-{% equation %}W\cap W^{\perp}=\left\{ 0\right\} {% endequation %}, מה שנובע מייד מכך שאם {% equation %}w\in W\cap W^{\perp}{% endequation %} אז {% equation %}\left\langle w,w\right\rangle =0{% endequation %} (כי {% equation %}w\in W{% endequation %} ו-{% equation %}w\in W^{\perp}{% endequation %} אורתוגונליים).

מה שאתם צריכים עכשיו להעלות בדמיון שלכם זה את {% equation %}\mathbb{R}^{2}{% endequation %} עם מערכת הצירים הרגילה - ציר {% equation %}x{% endequation %} וציר {% equation %}y{% endequation %} הם התת-מרחבים האורתוגונליים שנפרשים על ידי הוקטורים האורתונורמליים {% equation %}\left(1,0\right),\left(0,1\right){% endequation %} וההטלות על הצירים הללו הן ההטלות ה"רגילות" שאנו מכירים. הנה שוב קיבלנו הכללה של הגאומטריה המוכרת לנו.

טוב, מספיק להשתעשע, בפוסט הבא בנושא נעבור לאקשן האמיתי - מה קורה במפגש הענקים בין הטרנספורמציות הלינאריות והמכפלות הפנימיות.
