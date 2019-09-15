---
id: 3423
title: "קוסטים, משפט לגראנז' וחבורות מנה"
date: 2017-02-08 10:44:02
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - חבורות
  - חבורת מנה
  - משפט לגראנז'
  - קוסט
---
<a href="http://www.gadial.net/2017/02/07/subgroups_and_cyclic_groups/">בפוסט הקודם</a> של תורת החבורות דיברנו על תתי-חבורות והזכרתי את <strong>משפט לגראנז'</strong>. המשפט אומר שאם {% equation %}G{% endequation %} היא חבורה סופית, ו-{% equation %}H{% endequation %} היא תת-חבורה שלה, אז {% equation %}\left|H\right||\left|G\right|{% endequation %} - הסדר של {% equation %}H{% endequation %} מחלק את הסדר של {% equation %}G{% endequation %} ("סדר" של חבורה הוא מספר האיברים בה). כבר ראינו למשפט שני שימושים לא טריוויאליים - שכל חבורה מסדר ראשוני היא בהכרח ציקלית, ושאם לחבורה יש לכל היותר תת-חבורה אחת מכל סדר שמחלק את סדר החבורה, אז היא ציקלית. בפוסט הזה אני רוצה להוכיח את המשפט. ההוכחה תהיה מהסוג הטוב ביותר שאפשר - הוכחה שאנחנו נזקקים למושג חדש בשבילה, ומושג שיתגלה כשימושי, מועיל וחשוב מאין כמוהו בהמשך - המושג של <strong>קוסט</strong> (coset) של תת-חבורה.

<strong>קוסטים ומשפט לגראנז'</strong>

אישית, הרבה זמן לא הבנתי את המושג של קוסט, כי הכרתי את ההגדרה אבל לא את מה שהיא אומרת. אז נתחיל ממה שהיא אומרת, בנפנוף ידיים, ואז נראה דוגמאות: בהינתן חבורה {% equation %}G{% endequation %} ותת-חבורה {% equation %}H{% endequation %} שלה, <strong>קוסט</strong> של {% equation %}H{% endequation %} הוא קבוצה שמתקבלת על ידי "הזזה" של {% equation %}H{% endequation %}. בואו נראה שתי דוגמאות שבהן אפשר להרגיש את המשמעות של "הזזה" כזו בידיים.

נתחיל עם החבורה החביבה עלי, {% equation %}\mathbb{Z}{% endequation %}. בפוסט הקודם ראינו למה אני אוהב את החבורה הזו - זוהי החבורה הציקלית היחידה. ראינו שכל תת-חבורה של {% equation %}\mathbb{Z}{% endequation %} היא מהצורה {% equation %}n\mathbb{Z}=\left\{ 0,n,-n,2n,-2n,\dots\right\} {% endequation %} של הכפולות של מספר טבעי {% equation %}n{% endequation %} כלשהו. למשל, {% equation %}2\mathbb{Z}{% endequation %} היא חבורת הזוגיים. ומה על האי-זוגיים? בפוסט הקודם אמרתי שהם אינם חבורה, כי אינם סגורים לחיבור (ואינם כוללים את 0). אבל אפשר לחשוב עליהם בתור <strong>הזזה</strong> של הזוגיים צעד אחד ימינה. מספר זוגי הוא מספר מהצורה {% equation %}2k{% endequation %} עבור {% equation %}k\in\mathbb{Z}{% endequation %}, בעוד שמספר אי זוגי הוא מספר מהצורה {% equation %}2k+1{% endequation %} עבור {% equation %}k\in\mathbb{Z}{% endequation %}. כלומר, כל אי זוגי מתקבל מזוגי על ידי הוספה של 1. במתמטית, אומרים שהאי-זוגיים הם <strong>קוסט</strong> של הזוגיים בתוך חבורת השלמים. את האי-זוגיים אפשר לסמן באופן מקוצר בתור {% equation %}2\mathbb{Z}+1{% endequation %} - כאילו אנחנו מחברים 1 לכל תת-החבורה {% equation %}2\mathbb{Z}{% endequation %} (ניתן לסימון הזה פירוש פורמלי עוד מעט).

דבר דומה יקרה גם עם {% equation %}n=3{% endequation %}. קבוצת כל המספרים שמתחלקים ב-3, {% equation %}3\mathbb{Z}{% endequation %}, היא תת-חבורה של השלמים. קבוצת המספרים שמשאירים שארית 1 בחלוקה ב-3 היא לא תת-חבורה (אין את 0, אין סגירות) אבל היא קוסט של {% equation %}3\mathbb{Z}{% endequation %} ובדומה גם קבוצת המספרים שמשאירים שארית 2. את הקוסטים הללו מסמנים ב-{% equation %}3\mathbb{Z}+1{% endequation %} וב-{% equation %}3\mathbb{Z}+2{% endequation %}. הבנתם את העיקרון.

בשלב הזה אתם אולי שואלים - מה אם מזיזים ב-0? ובכן, בואו נדבר על הזוגיים למשל: {% equation %}2\mathbb{Z}+0=2\mathbb{Z}{% endequation %} - הזזה באפס מותירה אותנו עם הזוגיים. בפרט, הזוגיים הם גם כן קוסט של עצמם; אין עם זה בעיה. כמו כן, {% equation %}2\mathbb{Z}+2=2\mathbb{Z}{% endequation %}, כלומר גם הזזה במספר זוגי תיתן לנו את הקוסט של הזוגיים, והזזה ב-3 תיתן לנו את הקוסט של האי-זוגיים וכן הלאה. אותו קוסט יכול לפעמים להתקבל על ידי הזזה עבור יותר מערך אחד, ואין פה בעיה.

בואו נעבור לדוגמא אחרת, ציורית אף יותר, עם חבורה חדשה שטרם הצגתי - {% equation %}\mathbb{R}^{2}{% endequation %}. המישור. אוסף כל הנקודות מהצורה {% equation %}\left(a,b\right){% endequation %} כך ש-{% equation %}a,b\in\mathbb{R}{% endequation %} וחיבור הוא "איבר-איבר": {% equation %}\left(a,b\right)+\left(x,y\right)=\left(a+x,b+y\right){% endequation %}. לא קשה לראות שזו חבורה. עכשיו, בואו נסתכל על תת-החבורה הבאה: {% equation %}H=\left\{ \left(a,0\right)\ |\ a\in\mathbb{R}\right\} {% endequation %}. קל לבדוק שזו אכן תת-חבורה, והיא שווה פשוט לציר {% equation %}x{% endequation %} (האם זו חבורה ציקלית? יש אולי תחושה כזו, אבל לא: למשל, {% equation %}\left(1,0\right){% endequation %} הולך ליצור רק את האיברים מהצורה {% equation %}\left(n,0\right){% endequation %} כך ש-{% equation %}n\in\mathbb{Z}{% endequation %}, לא את כל הציר; חבורה ציקלית היא בהכרח בת-מניה ואילו {% equation %}H{% endequation %} לא בת מניה).

עכשיו, בואו ניקח את {% equation %}H{% endequation %} ונחבר לכל אבריה את {% equation %}\left(0,1\right){% endequation %} - וקטור היחידה האנכי. נקבל את מה שאסמן בתור {% equation %}H+\left(0,1\right)=\left\{ \left(a,1\right)\ |\ a\in\mathbb{R}\right\} {% endequation %}. הדבר הזה הוא הקו האופקי בגובה {% equation %}y=1{% endequation %}. זו לא תת-חבורה כי אין סגירות, אבל אפשר לחשוב על זה בתור "עותק" של ציר {% equation %}x{% endequation %} שפשוט הזזנו קצת למעלה. באופן דומה אם נחבר לכל אברי {% equation %}H{% endequation %} את {% equation %}\left(1,1\right){% endequation %} עדיין נקבל את אותו קוסט בדיוק - תחשבו על מה שקורה כשאתם לוקחים קו ישר אינסופי ומרימים אותו למעלה, ומה קורה כשאתם מרימים אותו באלכסון למעלה ושמאלה - מכיוון שהקו אינסופי, תקבלו בסופו של דבר את אותו הדבר בדיוק. לכן, כל עוד נחבר ל-{% equation %}H{% endequation %} איבר מהצורה {% equation %}\left(x,1\right){% endequation %}, ולא משנה מהו {% equation %}x{% endequation %}, נקבל את אותו קוסט. בקרוב נדון עוד בשאלה הזו, "מי האיברים שכשמחברים אותם לתת-החבורה מקבלים את אותו קוסט".

שאר הקוסטים של {% equation %}H{% endequation %} הם שאר הישרים האופקיים, והשאלה עכשיו היא מה קורה עם תת-חבורות דומות אחרות. למשל, {% equation %}H=\left\{ \left(a,a\right)\ |\ \left(a\in\mathbb{R}\right)\right\} {% endequation %}. זה תרגיל נחמד להראות שקוסט כאן הוא תמיד מהצורה {% equation %}H+\left(x,0\right)=\left\{ \left(a+x,a\right)\ |\ a\in\mathbb{R}\right\} {% endequation %} ויוצא שקוסט כזה הוא קו ישר עם שיפוע של 45 מעלות, כמו {% equation %}H{% endequation %} עצמה, אבל שנקודת החיתוך שלו עם ציר {% equation %}x{% endequation %} היא שונה מ-{% equation %}\left(0,0\right){% endequation %}. זה גם מה שיקרה באופן כללי: כל ישר שעובר דרך הראשית הוא תת-חבורה של {% equation %}\mathbb{R}^{2}{% endequation %}, ולכל ישר כזה, הקוסטים הם כל הישרים המקבילים לו. הנה איור:<strong>
<a href="{{site.baseurl}}{{site.post_images}}/2017/02/cosets.png" rel="attachment wp-att-3424"><img class="aligncenter size-large wp-image-3424" src="{{site.baseurl}}{{site.post_images}}/2017/02/cosets.png" alt="cosets" width="584" height="383" /></a></strong>

כאן תת-החבורה היא בשחור וחלק מהקוסטים האחרים שלה הם בצבעים עליזים. אני אומר <strong>חלק</strong> מהקוסטים כי אי אפשר לצייר את כולם - איחוד כל הקוסטים יתן לנו את כל המישור.

בואו נעבור כעת לפורמליזם. כזכור, כשאני מתאר חבורות כלליות אני משתמש בכפל, לא בחיבור, כדי לתאר את הפעולה של החבורה (להבדיל מהדוגמאות הקונקרטיות שהראיתי שבהן הפעולה הייתה ממש חיבור וכך היא סומנה) כמו כן, בדוגמאות שראינו החבורות היו אבליות ({% equation %}ab=ba{% endequation %}) בזמן שבאופן כללי אנחנו לא מניחים שחבורות הן אבליות, וזה הולך להשפיע על הטרמינולוגיה. בהינתן חבורה {% equation %}G{% endequation %}, תת-חבורה {% equation %}H{% endequation %} ואיבר {% equation %}a\in G{% endequation %} אני מסמן:

{% equation %}aH\triangleq\left\{ ah\ |\ h\in H\right\} {% endequation %}

{% equation %}Ha\triangleq\left\{ ha\ |\ h\in H\right\} {% endequation %}

הקבוצה {% equation %}aH{% endequation %} נקראת <strong>קוסט שמאלי</strong> של {% equation %}H{% endequation %} והקבוצה {% equation %}Ha{% endequation %} נקראת <strong>קוסט ימני</strong> של {% equation %}H{% endequation %}. צריך לשים לב לכך שקוסט יכול להיות בו זמנית גם שמאלי וגם ימני; אם החבורה היא אבלית זה בוודאי כך ({% equation %}aH=Ha{% endequation %} לכל {% equation %}a,H{% endequation %}) אבל גם בחבורה לא אבלית ייתכן שיתקיים {% equation %}aH=Ha{% endequation %}, או ייתכן שיתקיים {% equation %}aH=Hb{% endequation %} עבור {% equation %}a\ne b{% endequation %}. נחזור לזה עוד מעט.

בדוגמאות שלנו שמנו לב, אינטואיטיבית, לשני דברים: אם {% equation %}H{% endequation %} היא תת-חבורה של {% equation %}G{% endequation %}, אז:
<ul>
	<li>כל קוסט של {% equation %}H{% endequation %} "נראה כמו" {% equation %}H{% endequation %}. בפרט, הוא נראה "מאותו גודל" כמו {% equation %}H{% endequation %}.</li>
	<li>אוסף כל הקוסטים של {% equation %}H{% endequation %} מכסה את כל החבורה "בלי חפיפות".</li>
</ul>
השילוב של שתי התכונות הללו נותן לנו מייד את משפט לגראנז'. בואו ננסח אותן פורמלית.

התכונה הראשונה, פורמלית, פירושה שאם {% equation %}aH{% endequation %} הוא קוסט של {% equation %}H{% endequation %} (כנ"ל גם לקוסט ימני, אבל אני לא אטרח לעשות זאת במפורש, זו אותה הוכחה) אז קיימת פונקציה חח"ע ועל {% equation %}f:H\to aH{% endequation %}. בפרט, אם {% equation %}H{% endequation %} סופית אז {% equation %}\left|H\right|=\left|aH\right|{% endequation %}. קל לנחש מה {% equation %}f{% endequation %} אמורה להיות: {% equation %}f\left(h\right)=ah{% endequation %}. היא על פשוט בגלל ההגדרה של {% equation %}aH{% endequation %}. השאלה היא רק למה היא חח"ע, וזה נובע מהתכונה הבסיסית שהוכחתי בפוסט הראשון על חבורות: אם {% equation %}ax=ay{% endequation %} אז {% equation %}x=y{% endequation %}.

כעת לתכונה השניה, שבעצם אומרת שני דברים. ראשית, שכל {% equation %}a\in G{% endequation %} שייך לקוסט <strong>כלשהו</strong> של {% equation %}H{% endequation %}. זה די מובן מאליו: {% equation %}a\in aH{% endequation %} שכן {% equation %}e\in H{% endequation %} ולכן {% equation %}a=a\cdot e\in aH{% endequation %}. הדבר השני והמעניין יותר הוא שלא קיים {% equation %}a{% endequation %} כך ש-{% equation %}a\in xH{% endequation %} וגם {% equation %}a\in yH{% endequation %} עבור {% equation %}xH\ne yH{% endequation %}. בואו נוכיח את זה בגישה "חיובית": נניח ש-{% equation %}a\in xH{% endequation %} ו-{% equation %}a\in yH{% endequation %} ונוכיח שנובע מכך ש-{% equation %}xH=yH{% endequation %}.

אם כן, נניח ש-{% equation %}a\in xH{% endequation %}, כלומר קיים {% equation %}h_{1}{% endequation %} כך ש-{% equation %}a=xh_{1}{% endequation %}. באופן דומה, מכיוון ש-{% equation %}a\in yH{% endequation %} קיים {% equation %}h_{2}{% endequation %} כך ש-{% equation %}a=yh_{2}{% endequation %}. זה אומר ש-{% equation %}xh_{1}=yh_{2}{% endequation %}, כלומר {% equation %}x=yh_{2}h_{1}^{-1}{% endequation %}. כעת, שימו לב לאיבר {% equation %}h_{2}h_{1}^{-1}{% endequation %}. מכיוון ש-{% equation %}H{% endequation %} היא <strong>תת-חבורה</strong>, אנחנו יודעים שגם {% equation %}h_{2}h_{1}^{-1}\in H{% endequation %} (אם {% equation %}H{% endequation %} לא הייתה תת-חבורה כל הסיפור היה נשבר ברגע זה ממש). כעת בואו ניקח איבר <strong>כלשהו</strong> ב-{% equation %}xH{% endequation %}. הוא מהצורה {% equation %}xh=\left(yh_{2}h_{1}^{-1}\right)h=y\left(h_{2}h_{1}^{-1}h\right)\in yH{% endequation %}. קיבלנו ש-{% equation %}xH\subseteq yH{% endequation %} ובאותו האופן מראים ש-{% equation %}yH\subseteq xH{% endequation %}, ומכאן ש-{% equation %}xH=yH{% endequation %}.

משפט לגראנז' נובע כעת כמעט מאליו. מה שראינו הוא ש-{% equation %}G=\bigcup aH{% endequation %} כאשר האיחוד נלקח על כל הקוסטים של {% equation %}H{% endequation %} (דהיינו, אותו קוסט לא מופיע באיחוד פעמיים; אנחנו בוחרים {% equation %}a{% endequation %} כלשהו כך ש-{% equation %}aH{% endequation %} נותן את הקוסט, וחסל; אם יש עוד {% equation %}b{% endequation %} כך ש-{% equation %}bH{% endequation %} הוא אותו קוסט הוא לא ישתתף באיחוד כי לא צריך אותו). מכיוון שזה איחוד זר, אז במקרה של חבורה סופית, שבו יש מספר סופי של קוסטים, אפשר לכתוב {% equation %}\left|G\right|=\left|\bigcup aH\right|=\sum\left|aH\right|{% endequation %} כאשר הסכום נלקח על כל הקוסטים. כעת, למספר הקוסטים של {% equation %}H{% endequation %} ב-{% equation %}G{% endequation %} יש שם מקובל: <strong>האינדקס</strong> של {% equation %}H{% endequation %} ב-{% equation %}G{% endequation %}, וסימון מקובל: {% equation %}\left|G:H\right|{% endequation %}. מכיוון שראינו ש-{% equation %}\left|aH\right|=\left|H\right|{% endequation %} נקבל את השוויון הבא: {% equation %}\left|G\right|=\left|G:H\right|\cdot\left|H\right|{% endequation %}. השוויון הזה הוא בדיוק משפט לגראנז': הסדר של {% equation %}H{% endequation %} מחלק את הסדר של {% equation %}G{% endequation %}, והמנה של החלוקה היא בדיוק האינדקס של {% equation %}H{% endequation %} ב-{% equation %}G{% endequation %}. מה שכן, שימו לב שהאינדקס הוא מספר מעניין גם כש-{% equation %}G{% endequation %} <strong>אינסופית</strong>; בהחלט ייתכן שיש תת-חבורה מאינדקס סופי גם כש-{% equation %}G{% endequation %} אינסופית (למשל, האינדקס של {% equation %}2\mathbb{Z}{% endequation %} ב-{% equation %}\mathbb{Z}{% endequation %} הוא 2, כפי שראינו).

עכשיו בואו נעצור, ננשום אוויר ונעבור לנושא שבהתחלה ייראה קצת לא קשור, אבל הוא כמובן קשור בצורה הדוקה ביותר למה שעשינו עד כה ונראה זאת עד סוף הפוסט.

<strong>חבורות מנה</strong>

עבור חבורה {% equation %}G{% endequation %} ראינו דרך אחת להבין מה הולך בה - מסתכלים על <strong>תת-החבורות</strong> שלה. תת-חבורה הייתה תת-קבוצה של {% equation %}G{% endequation %} שהפעולה הבינארית של {% equation %}G{% endequation %} <strong>משרה עליה</strong> פעולה בינארית משל עצמה שביחס אליה היא חבורה. תת-חבורה, אם כן, היא מה שמקבלים כשמסלקים חלק מהאיברים ורואים מה קורה עם היתר. עכשיו אני רוצה לדבר על מושג נוסף, חשוב באותה מידה כמו תת-חבורה: <strong>חבורת מנה</strong>. חבורת מנה היא מה שמתקבל מ-{% equation %}G{% endequation %} כשלוקחים איברים ובמקום לסלק אותם, אנחנו <strong>מאחדים</strong> אותם. פורמלית, מה קורה כשאנחנו לוקחים <strong>יחס שקילות</strong> על {% equation %}G{% endequation %}.

אם אתם מכירים יחסי שקילות, מצוין. אם לא, אני אנסה לתת את הדוגמה הכי יומיומית במתמטיקה שאני מכיר: מספרים רציונליים. מה זה מספר רציונלי אנחנו יודעים - "חצי" זה מושג שדי ברור לנו. אבל מהר מאוד כשמתחילים להתעסק עם מספרים כאלו רואים שיש לנו יותר מדרך אחת לכתוב "חצי". אפשר לכתוב {% equation %}\frac{1}{2}{% endequation %} ואפשר לכתוב {% equation %}\frac{2}{4}{% endequation %} ואפשר לכתוב {% equation %}\frac{123}{246}{% endequation %} וכן הלאה. מבחינתנו כל הביטויים הללו הם שקולים זה לזה - הם מייצגים את אותו דבר. פורמלית, כשאנחנו מדברים על המספרים הרציונליים אנחנו מסתכלים על הקבוצה {% equation %}\left\{ \frac{a}{b}\ |\ a\,b\in\mathbb{Z},b\ne0\right\} {% endequation %} כש-{% equation %}\frac{a}{b}{% endequation %} כאן לא בא לבטא פעולת חילוק (כי לא מוגדר לנו חילוק על {% equation %}\mathbb{Z}{% endequation %} באופן כללי) אלא זהו פשוט סימון; ואז אנחנו באים ורוצים לומר שהסימון {% equation %}\frac{1}{2}{% endequation %} והסימון {% equation %}\frac{2}{4}{% endequation %} מסמנים את אותו הדבר. באופן כללי, {% equation %}\frac{a}{b}{% endequation %} ו-{% equation %}\frac{c}{d}{% endequation %} מייצגים את אותו דבר אם {% equation %}c\cdot b=a\cdot d{% endequation %}.

<strong>יחס שקילות</strong> מעל קבוצה {% equation %}A{% endequation %} הוא אוסף של זוגות {% equation %}\left(x,y\right){% endequation %} כך ש-{% equation %}x,y\in A{% endequation %}, שמקיים שלוש דרישות: ראשית, לכל {% equation %}x\in A{% endequation %} מתקיים ש-{% equation %}\left(x,x\right){% endequation %} שייך ליחס (<strong>רפלקסיביות</strong>). שנית, אם {% equation %}\left(x,y\right){% endequation %} שייך ליחס כך גם {% equation %}\left(y,x\right){% endequation %} (<strong>סימטריה</strong>) ולבסוף, אם {% equation %}\left(x,y\right){% endequation %} וגם {% equation %}\left(y,z\right){% endequation %}שייכים ליחס כך גם {% equation %}\left(x,z\right){% endequation %} (<strong>טרנזיטיביות</strong>).

אם {% equation %}R{% endequation %} הוא יחס שקילות ו-{% equation %}x\in A{% endequation %} הוא איבר כלשהו, מסמנים את קבוצת כל האיברים ששקולים ל-{% equation %}x{% endequation %} על פי היחס {% equation %}R{% endequation %} ב-{% equation %}\left[x\right]_{R}\triangleq\left\{ y\in A\ |\ \left(x,y\right)\in R\right\} {% endequation %}. לרוב אפילו סתם כותבים {% equation %}\left[x\right]{% endequation %} אם ברור לאיזה {% equation %}R{% endequation %} מתכוונים. לקבוצה כזו קוראים <strong>מחלקת שקילות</strong>. בהינתן מחלקה, כל איבר {% equation %}x{% endequation %} כך ש-{% equation %}\left[x\right]{% endequation %} היא המחלקה הזו נקרא <strong>נציג</strong> של המחלקה. בדוגמה שלנו, {% equation %}\left[\frac{1}{2}\right]=\left[\frac{2}{4}\right]{% endequation %} וכדומה - מחלקת השקילות הזו מסמלת את המספר "חצי" עם נציגים כמו {% equation %}\frac{1}{2}{% endequation %} ו-{% equation %}\frac{1}{4}{% endequation %}. כפי שאנחנו רואים, איברים שונים עשויים להגדיר את אותה מחלקת שקילות. קצת מזכיר את האופן שבו איברים שונים מגדירים את אותו קוסט, נכון?

את אוסף מחלקות השקילות של {% equation %}A{% endequation %} על פי היחס {% equation %}R{% endequation %} מסמנים ב-{% equation %}A/R{% endequation %} וקוראים לו <strong>קבוצת המנה</strong> של {% equation %}A{% endequation %} על פי {% equation %}R{% endequation %}. עכשיו, התכונות של יחס שקילות מבטיחות שקבוצת המנה תהיה נחמדה: ראשית, אין כזה דבר מחלקת שקילות ריקה; שנית, האיחוד של כל מחלקות השקילות נותן את כל {% equation %}A{% endequation %}; ולבסוף, אין חפיפה - שתי מחלקות שקילות הן זרות או זהות. פורמלית אומרים שקבוצת המנה מהווה <strong>חלוקה</strong> של {% equation %}A{% endequation %}. נשמע בדיוק כמו מה שקרה לנו עם קוסטים? כמובן, זה לא מקרי...

הכיוון השני גם נכון: כל חלוקה של {% equation %}A{% endequation %} מגדירה יחס שקילות (שני איברים הם שקולים אם הם באותה קבוצה בחלוקה) כך שקבוצת המנה על פי יחס השקילות הזה היא החלוקה שממנה התחלנו. במילים אחרות, יחסי שקילות וחלוקות הן שתי דרכי ייצוג שונות לאותו הדבר, ואנחנו משתמשים במה שנוח לנו בכל רגע נתון.

איך כל זה קשור לחבורות? ובכן, חבורה היא גם קבוצה, אז אפשר להגדיר עליה שלל יחסי שקילות. למשל, על {% equation %}\mathbb{Z}{% endequation %} בואו נגדיר את יחס השקילות שבו {% equation %}\left(x,y\right){% endequation %} שקולים אם ורק אם {% equation %}xy\ge1{% endequation %} או ש-{% equation %}x=y=0{% endequation %}. ליחס הזה יש שלוש מחלקות שקילות: החיוביים {% equation %}\mathbb{Z}^{+}{% endequation %}, השליליים {% equation %}\mathbb{Z}^{-}{% endequation %} ו-{% equation %}\left\{ 0\right\} {% endequation %}. וכעת אני מתעניין בשאלה הבאה: האם קבוצת המנה של {% equation %}\mathbb{Z}{% endequation %} על פי יחס השקילות הזה היא חבורה?

ובכן, אנחנו כבר יודעים שיש בדיוק חבורה אחת עם שלושה איברים, {% equation %}\mathbb{Z}_{3}{% endequation %}, ואפשר להגדיר פעולה על מחלקות השקילות בהתאם. למשל לומר ש-{% equation %}\mathbb{Z}^{+}\cdot\mathbb{Z}^{+}=\mathbb{Z}^{-}{% endequation %} וש-{% equation %}\left\{ 0\right\} {% endequation %} הוא איבר היחידה וכדומה. אבל אנחנו מרגישים שזה לא מעניין: לקחנו קבוצה {% equation %}\mathbb{Z}{% endequation %} שהיא גם חבורה, חילקנו אותה למחלקות שקילות, ואז הגדרנו פעולה חדשה על מחלקות השקילות מהראש שלנו. זה שהתחלנו מראש עם חבורה לא בא לידי ביטוי - הפעולה של החבורה המקורית לא באה לידי ביטוי בבניה שלנו, אז מה עשינו פה?

השאלה היא, כמובן, באיזה מובן אני רוצה שהפעולה של החבורה המקורית תבוא לידי ביטוי. אז הנה ההצעה שלי, שתשפיע על כל מה שנעשה מכאן והלאה: אם יש לי חבורה {% equation %}G{% endequation %} ויחס שקילות {% equation %}R{% endequation %} שמוגדר עליה, אני רוצה למצוא פעולת כפל על מחלקות השקילות של {% equation %}G{% endequation %} באופן כזה שכדי לכפול שתי מחלקות שקילות מה שאפשר יהיה לעשות הוא לבחור נציג לכל מחלקת שקילות, לכפול את הנציגים על פי הפעולה של {% equation %}G{% endequation %}, ואז לקחת את מחלקת השקילות של התוצאה. פורמלית, אני רוצה שיתקיים {% equation %}\left[a\right]\cdot\left[b\right]=\left[ab\right]{% endequation %}, ואני רוצה שבמקרה הזה, קבוצת המנה תהווה חבורה ביחס לפעולה הזו.

מהדרישה הזו נובע המון על יחס השקילות {% equation %}R{% endequation %} עצמו - מה הוא בדיוק יכול להיות ואיך הוא צריך להתנהג. ראשית, שימו לב לכך שאם נציב {% equation %}b=e{% endequation %} נקבל שצריך להתקיים {% equation %}\left[a\right]\cdot\left[e\right]=\left[a\cdot e\right]=\left[a\right]{% endequation %}. זה אומר ש-{% equation %}\left[e\right]{% endequation %} הולך להיות איבר היחידה של חבורת המנה. באופן דומה, {% equation %}\left[a\right]\cdot\left[a^{-1}\right]=\left[aa^{-1}\right]=\left[e\right]{% endequation %} ולכן {% equation %}\left[a^{-1}\right]=\left(\left[a\right]\right)^{-1}{% endequation %} - ההופכי של מחלקת השקילות של {% equation %}a{% endequation %} מיוצג על ידי ההופכי של {% equation %}a{% endequation %}.

כעת, בואו ניקח {% equation %}x,y\in\left[e\right]{% endequation %} כלשהם. אז {% equation %}\left[xy^{-1}\right]=\left[x\right]\cdot\left[y\right]^{-1}=\left[e\right]\cdot\left[e\right]^{-1}=\left[e\right]{% endequation %} (כאן אני משתמש בכך שאם {% equation %}x\in\left[e\right]{% endequation %} אז {% equation %}\left[x\right]=\left[e\right]{% endequation %}). במילים: אם {% equation %}x,y\in\left[e\right]{% endequation %} אז גם {% equation %}xy^{-1}\in\left[e\right]{% endequation %}. את הדבר הזה ראינו בפוסט הקודם - המשמעות שלו היא ש-{% equation %}\left[e\right]{% endequation %} היא <strong>תת-חבורה</strong> של {% equation %}G{% endequation %}. אז בואו נסמן {% equation %}H=\left[e\right]{% endequation %} מעתה ואילך.

כעת, בואו נניח ש-{% equation %}\left[a\right]=\left[b\right]{% endequation %}, כלומר {% equation %}a,b{% endequation %} שקולים זה לזה. אז {% equation %}\left[b\right]^{-1}\left[a\right]=\left[e\right]{% endequation %} (כפלתי את שני האגפים ב-{% equation %}\left[b\right]^{-1}{% endequation %}), כלומר {% equation %}\left[b^{-1}a\right]=\left[e\right]{% endequation %}, כלומר {% equation %}b^{-1}a\in H{% endequation %}. אפשר גם להפוך את כיוון הגרירות ולקבל שאם {% equation %}b^{-1}a\in H{% endequation %} אז {% equation %}\left[a\right]=\left[b\right]{% endequation %}. במילים אחרות, קיבלנו שאם עבור יחס שקילות כלשהו קבוצת המנה שמקבלים היא חבורה עם הפעולה שמושרית מ-{% equation %}G{% endequation %}, אז יחס השקילות <strong>חייב</strong> להיות מהצורה הבאה: קיימת תת-חבורה {% equation %}H{% endequation %} של {% equation %}G{% endequation %} כך ש-{% equation %}a,b{% endequation %} שקולים אם ורק אם {% equation %}b^{-1}a\in H{% endequation %}.

אם זהו יחס השקילות, האם יש לנו תיאור מפורש של מחלקות השקילות? כמובן. {% equation %}\left[a\right]{% endequation %} כוללת את כל האיברים {% equation %}b\in G{% endequation %} כך ש-{% equation %}b^{-1}a\in H{% endequation %}, כלומר כך שקיים {% equation %}h\in H{% endequation %} עבורו {% equation %}b^{-1}a=h{% endequation %}, כלומר ש-{% equation %}b=ah^{-1}{% endequation %}. במילים אחרות, {% equation %}\left[a\right]=\left\{ ah\ |\ h\in H\right\} =aH{% endequation %}. קיבלנו שמחלקת השקילות של {% equation %}a{% endequation %} היא בדיוק הקוסט השמאלי של {% equation %}H{% endequation %} שנקבע על ידי {% equation %}a{% endequation %}. באופן כללי, כל מחלקות השקילות של היחס יהיו כל הקוסטים השמאליים של {% equation %}H{% endequation %}, מה שמסביר את הדמיון בין קוסטים ובין חלוקות - קוסטים הם פשוט מקרה פרטי של חלוקה. מעכשיו אני לא אטרח לכתוב {% equation %}\left[a\right]{% endequation %} יותר - אני פשוט אכתוב {% equation %}aH{% endequation %}, כי כבר ברור על מה מדובר פה.

בשלב הזה אולי קופצת נורת אזהרה אצל חלקכם. אם כן, זה מצוין, כי יש הונאה כלשהי בדרך שבה הצגתי את הדברים, אבל לפני שנלך לשם בואו נראה דוגמא. וזו תהיה, איך לא, הדוגמא של {% equation %}\mathbb{Z}{% endequation %}. כאשר {% equation %}H=2\mathbb{Z}{% endequation %}, ראינו כבר שהקוסטים הם הזוגיים והאי-זוגיים. מהו יחס השקילות? הכתיב {% equation %}b^{-1}a\in H{% endequation %} מתורגם במקרה הזה ל-{% equation %}a-b\in2\mathbb{Z}{% endequation %}, או בניסוח אחר - {% equation %}2{% endequation %} מחלק את {% equation %}a-b{% endequation %}. זה בדיוק יחס השקילות שבדרך כלל מסומן במתמטיקה בתור {% equation %}a\equiv b\left(\text{mod }2\right){% endequation %}. באופן דומה עבור {% equation %}n\mathbb{Z}{% endequation %} נקבל את יחס השקילות מודולו {% equation %}n{% endequation %}. ומה חבורות המנה שאנחנו מקבלים? בפוסט הזה אציג את הפורמליזם המדויק ואוכיח זאת, אבל לא קשה לראות ש-{% equation %}\mathbb{Z}/n\mathbb{Z}{% endequation %} זו בערך אותה חבורה כמו {% equation %}\mathbb{Z}_{n}{% endequation %}, עד כדי זה שאברי {% equation %}\mathbb{Z}_{n}{% endequation %} הם מספרים טבעיים בתחום מסויים ואברי {% equation %}\mathbb{Z}/n\mathbb{Z}{% endequation %} הם קבוצות של טבעיים.

זה מעניין, כי זה מצביע על כך שבחבורה הציקלית האינסופית היחידה, {% equation %}\mathbb{Z}{% endequation %}, מסתתרת האינפורמציה של כל החבורות הציקליות הסופיות - רק שהן מסתתרות לא בתור תת-חבורות של {% equation %}\mathbb{Z}{% endequation %} (כל תת-החבורות של {% equation %}\mathbb{Z}{% endequation %} הן ציקליות שנראות כמו {% equation %}\mathbb{Z}{% endequation %}) אלא בתוך המנות של {% equation %}\mathbb{Z}{% endequation %}. זו אינטואיציה ראשונה לכך ש"להבין את המנות של החבורה עוזר להבין את המבנה שלה".

אוקיי, אם הכל טוב, אז מה בעצם רע? נורית האזהרה שאמורה לקפוץ היא שאמרתי שמחלקות השקילות של היחס הן הקוסטים <strong>השמאליים</strong> של {% equation %}H{% endequation %}. למה דווקא השמאליים? מה זה חוסר הסימטריה הזה? מה עשיתי שהצדיק אותו? התשובה היא שהתחלתי עם המשוואה {% equation %}\left[a\right]=\left[b\right]{% endequation %} והגעתי ממנה אל {% equation %}b^{-1}a\in H{% endequation %}. אבל באותה מידה יכלתי להגיע ממנה גם אל {% equation %}ab^{-1}\in H{% endequation %} (תנסו!) ואז הייתי מגיע למסקנה שמחלקות השקילות הן הקוסטים <strong>הימניים</strong> של {% equation %}H{% endequation %}. בפרט, מחלקת השקילות של {% equation %}a{% endequation %} הייתה גם הקוסט {% equation %}aH{% endequation %} וגם הקוסט {% equation %}Ha{% endequation %}, דהיינו {% equation %}aH=Ha{% endequation %}. זה עלול להיראות בטעות כאילו הוכחתי שבחבורה כללית תמיד מתקיים ש-{% equation %}aH=Ha{% endequation %} ולכן לא ברור למה מלכתחילה טרחתי להבדיל בין קוסטים ימניים לשמאליים. האמת היא שלא הוכחתי שום דבר כזה. התחלתי מ<strong>להניח שהפעולה על הקוסטים מגדירה חבורה</strong> וזו הנחה כבדה. מה שהראיתי פה הוא שהדרישה שיתקיים {% equation %}aH=Ha{% endequation %} לכל {% equation %}a\in G{% endequation %} היא <strong>תנאי הכרחי</strong> ש-{% equation %}H{% endequation %} צריכה לקיים אם אנחנו רוצים שהפעולה של {% equation %}G{% endequation %} תשרה מבנה של חבורה על אוסף הקוסטים של {% equation %}H{% endequation %}. כדי להשלים את הפוסט אני ארצה להוכיח שזה גם תנאי מספיק - כלומר, שאם {% equation %}H{% endequation %} היא תת-חבורה עבורה מתקיים {% equation %}aH=Ha{% endequation %} לכל {% equation %}a\in G{% endequation %}, אז הפעולה {% equation %}aH\cdot bH\triangleq\left(ab\right)H{% endequation %} היא <strong>מוגדרת היטב</strong> ואוסף הקוסטים של {% equation %}H{% endequation %} הוא חבורה ביחס אליה.

צריך להסביר את ה"מוגדר היטב" הזה. כפי שכבר ראינו, קוסט אפשר לייצג על ידי הרבה איברים. למשל, {% equation %}2\mathbb{Z}+1=2\mathbb{Z}+3{% endequation %}. אבל את הפעולה שלי על הקוסטים אני מגדיר <strong>על פי הנציגים</strong>. כלומר, אני אומר: רוצים לכפול שני קוסטים? נהדר. תבחרו <strong>באקראי</strong> שני איברים, אחד מכל קוסט, תכפלו את האיברים הללו וקחו את הקוסט של התוצאה. כדי שהפעולה הזו תהיה מוגדרת היטב אני צריך להראות שלא משנה אילו נציגים אני אבחר לכל קוסט, אני אקבל תמיד את אותו פלט. אחרת ה"פעולה" {% equation %}aH\cdot bH\triangleq\left(ab\right)H{% endequation %} היא בכלל לא פונקציה אלא בולשיט.

למרבה המזל, ההוכחה פשוטה. בואו ניקח {% equation %}a_{1},a_{2}{% endequation %} כך ש-{% equation %}a_{1}H=a_{2}H{% endequation %} וניקח {% equation %}b_{1},b_{2}{% endequation %} כך ש-{% equation %}b_{1}H=b_{2}H{% endequation %}. אני צריך להראות ש-{% equation %}\left(a_{1}b_{1}\right)H=\left(a_{2}b_{2}\right)H{% endequation %} (כלומר, שלכל שתי בחירות אפשריות שונות של נציגים אני אקבל את אותה תוצאה, מה שמבטיח תוצאה זהה לכל בחירת נציגים). כבר ראינו קודם שבשביל להראות את זה, מספיק להראות ש-{% equation %}a_{2}b_{2}\in\left(a_{1}b_{1}\right)H{% endequation %}, כלומר שקיים {% equation %}h{% endequation %} כך ש-{% equation %}a_{2}b_{2}=a_{1}b_{1}h{% endequation %}.

כעת, {% equation %}a_{1}H=a_{2}H{% endequation %} פירושו שקיים {% equation %}h_{a}{% endequation %} כך ש-{% equation %}a_{2}=a_{1}h_{a}{% endequation %}. בדומה, {% equation %}b_{1}H=b_{2}H{% endequation %} פירושו שקיים {% equation %}h_{b}{% endequation %} כך ש-{% equation %}b_{2}=b_{1}h_{b}{% endequation %}. אם כן:

{% equation %}a_{2}b_{2}=\left(a_{1}h_{a}\right)\left(b_{1}h_{b}\right)=a_{1}\left(h_{a}b_{1}\right)h_{b}{% endequation %}

שימו לב ל-{% equation %}h_{a}b_{1}{% endequation %} הזה! לו רק יכלנו להחליף את הסדר של שני אלו, היינו מקבלים {% equation %}a_{1}b_{1}\left(h_{a}h_{b}\right){% endequation %} והכל היה מסתדר! בחבורה אבלית אנחנו באמת יכולים להחליף והכל בסדר; אבל בחבורות לא אבליות זה לאו דווקא המצב. אז מה עושים? משתמשים בהנחה שלנו: {% equation %}bH=Hb{% endequation %}. מכיוון ש- {% equation %}h_{a}b_{1}\in Hb{% endequation %} אז נקבל {% equation %}h_{a}b_{1}\in bH{% endequation %}, מה שאומר שקיים {% equation %}h^{\prime}{% endequation %} כך ש-{% equation %}h_{a}b_{1}=b_{1}h^{\prime}{% endequation %}, ואז אנחנו מקבלים {% equation %}a_{2}b_{2}=a_{1}b_{1}\left(h^{\prime}h_{b}\right){% endequation %} והכל מסתדר. במילים אחרות, {% equation %}bH=Hb{% endequation %} אומר ש-{% equation %}H{% endequation %} מקיימת "סוג של קומוטטיביות" עם יתר החבורה: איבר כלשהו של החבורה לא מתחלף בכפל בהכרח עם אברי {% equation %}H{% endequation %}, אבל אפשר להחליף אותו בכפל עם איבר של {% equation %}H{% endequation %} ב"מחיר" של שינוי האיבר הזה של {% equation %}H{% endequation %} לאיבר <strong>אחר</strong> של {% equation %}H{% endequation %}. תת-חבורה {% equation %}H{% endequation %} של {% equation %}G{% endequation %} שהיא בעלת התכונה הזו, ש-{% equation %}aH=Ha{% endequation %} לכל {% equation %}a\in G{% endequation %}, נקראת <strong>תת-חבורה נורמלית</strong>, ועוד רגע נראה עוד דרכים להגדיר אותה.

מה שהראינו היה שהפעולה {% equation %}aH\cdot bH\triangleq\left(ab\right)H{% endequation %} על הקוסטים היא מוגדרת היטב. זה עדיין לא מוכיח שהקוסטים הם חבורה ביחס לפעולה הזו. יש לנו שלוש אקסיומות לטפל בהן. שתיים מהן, למרבה המזל, טריוויאליות ובעצם כבר ראינו אותן: {% equation %}eH=H{% endequation %} היא בבירור איבר היחידה הכפלי (כי {% equation %}aH\cdot eH=\left(ae\right)H=aH{% endequation %}). בדומה, לכל {% equation %}aH{% endequation %} קיים הופכי: {% equation %}a^{-1}H{% endequation %}. מה שבעצם נותר הוא האסוציאטיביות. בניגוד למקרה של תת-חבורה, שם האסוציאטיביות "נורשת" מהפעולה המקורית, כאן בכל זאת צריך לעבור ולוודא בזהירות שאין בעיה:

{% equation %}aH\cdot\left(bH\cdot cH\right)=aH\cdot\left(bc\right)H=\left(a\left(bc\right)\right)H=\left(\left(ab\right)c\right)H=abH\cdot cH=\left(aH\cdot bH\right)\cdot cH{% endequation %}

שום דבר מסובך, ובסופו של דבר האסוציאטיביות מתקבלת מכך שהפעולה ב-{% equation %}G{% endequation %} המקורית הייתה אסוציאטיבית. זה מסיים את כל העסק הזה - אנחנו עכשיו רואים איך קוסטים צצים להם באופן טבעי כשמדברים על חבורות מנה, ומה אלו חבורות מנה בכלל, ויש לנו גם את המושג החדש של תת-חבורה נורמלית.

לסיום, אני רוצה לתת עוד אפיון למה זו תת-חבורה נורמלית, שהוא לרוב פופולרי קצת יותר (אבל לא צץ לי באופן "טבעי" פה, אז לא התחלתי ממנו). לצורך כך אני אציג מושג חדש: <strong>הצמדה</strong>. הצמדה זה משהו שהוא טריוויאלי בחבורות אבליות, ולכן עד כה לא ממש ראינו דוגמאות אליו כי התעסקתי בעיקר בחבורות אבליות. אם {% equation %}a{% endequation %} הוא איבר כלשהו של {% equation %}G{% endequation %} ואילו {% equation %}g{% endequation %} הוא איבר אחר, אז <strong>ההצמדה </strong>של {% equation %}a{% endequation %} על ידי {% equation %}g{% endequation %} היא האיבר {% equation %}gag^{-1}{% endequation %}. זו פעולה שנראית מוזרה במבט ראשון, אבל סטודנטים למתמטיקה נתקלים בה כבר בקורס בסיסי באלגברה לינארית: אם {% equation %}A{% endequation %} היא מטריצה שמייצגת טרנספורמציה לינארית בבסיס כלשהו, ו-{% equation %}P{% endequation %} היא מטריצת מעבר אל הבסיס הזה מבסיס אחר, אז {% equation %}PAP^{-1}{% endequation %} תהיה המטריצה שמייצגת את הטרנספורמציה ש-{% equation %}A{% endequation %} מייצגת, רק בבסיס האחר. דוגמה אחרת היא עם פעולות של סיבוב ושיקוף (שאכן מהוות חבורה): תפתחו תוכנת ציור עם תמונה אהובה, תבצעו לתמונה שיקוף, אחר כך סיבוב ב-90 מעלות ימינה, אחר כך שוב שיקוף (שיקוף הוא ההופכי של עצמו). מה קרה? פעולות השיקוף לפני ואחרי גרמו לשינוי של טרנספורמציית הסיבוב.

בחבורה אבלית, {% equation %}gag^{-1}=agg^{-1}=a{% endequation %} ולכן אין פה משהו מעניין, אבל בחבורות לא אבליות, כפי שראינו, בהחלט מדובר על פעולה לא טריוויאלית. ואם הגדרנו אותה על איברים בודדים, אפשר להגדיר אותה גם על חבורות: {% equation %}aHa^{-1}=\left\{ aha^{-1}\ |\ h\in H\right\} {% endequation %}. כעת, הגדרה שקולה של תת-חבורה נורמלית הוא בתור תת-חבורה {% equation %}H{% endequation %} שמקיימת {% equation %}aHa^{-1}=H{% endequation %} לכל {% equation %}a\in G{% endequation %}. למה זה נכון? אינטואיטיבית, כי בואו נכפול את המשוואה {% equation %}aHa^{-1}=H{% endequation %} ב-{% equation %}a{% endequation %} מצד ימין... אבל זו לא פורמליסטיקה. ברמה הפורמליסטית, אם {% equation %}aH=Ha{% endequation %} אז {% equation %}aha^{-1}=h^{\prime}aa^{-1}=h^{\prime}\in H{% endequation %} על פי הכלל שראינו קודם של "אפשר להחליף אם מחליפים" שזה ניסוח לא מבלבל בכלל. זה מוכיח ש-{% equation %}aHa^{-1}\subseteq H{% endequation %}. הכיוון הבודד הזה מספיק: אם {% equation %}aHa^{-1}\subseteq H{% endequation %} לכל {% equation %}a{% endequation %}, אז אינטואיטיבית נכפול את המשוואה הזו משמאל ב-{% equation %}a^{-1}{% endequation %} ומימין ב-{% equation %}a{% endequation %} ונקבל {% equation %}H\subseteq a^{-1}Ha{% endequation %} לכל {% equation %}a{% endequation %}, ובפרט עבור הצבה של {% equation %}a^{-1}{% endequation %} במקום {% equation %}a{% endequation %} נקבל {% equation %}H\subseteq aHa^{-1}{% endequation %}. פורמלית, אם לכל {% equation %}h\in H{% endequation %} מתקיים ש-{% equation %}aha^{-1}\in H{% endequation %} אז קיים {% equation %}h^{\prime}{% endequation %} כך ש-{% equation %}aha^{-1}=h^{\prime}{% endequation %}, כלומר {% equation %}h=a^{-1}h^{\prime}a\in a^{-1}Ha{% endequation %}, כנדרש.

נשאר רק הכיוון השני, לפיו אם {% equation %}aHa^{-1}=H{% endequation %} לכל {% equation %}a{% endequation %} אז {% equation %}aH=Ha{% endequation %} לכל {% equation %}a{% endequation %}. אפשר אפילו להסתפק בהנחה ש-{% equation %}aHa^{-1}\subseteq H{% endequation %} כי כבר ראינו שהיא גוררת את השוויון. ניקח איבר של {% equation %}aH{% endequation %}, נאמר {% equation %}ah{% endequation %}. אז אנחנו יודעים ש-{% equation %}ah\cdot a^{-1}\in H{% endequation %}, כלומר {% equation %}ah\cdot a^{-1}=h^{\prime}{% endequation %}, כלמר {% equation %}ah=h^{\prime}a\in Ha{% endequation %} וזה מה שרצינו. זה מסיים את האפיון הזה של תת-חבורות נורמליות, שלעתים קרובות הוא נוח יותר לעבודה מאפיון ה"קוסט שמאלי הוא קוסט ימני".

בפוסט הבא - סוף סוף נתחיל לפרמל את נפנוף הידיים שלי של "היי תראו! החבורות הללו הן בדיוק אותו דבר בערך!"