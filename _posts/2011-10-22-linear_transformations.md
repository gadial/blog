---
id: 1389
title: "טרנספורמציות לינאריות"
date: 2011-10-22 20:03:52
layout: post
categories: 
  - אלגברה לינארית
tags: 
  - אלגברה לינארית
  - טרנספורמציות לינאריות
---
עד עכשיו בפוסטים על אלגברה לינארית דיברתי על מרחבים וקטוריים, כלומר על אובייקט מתמטי שמקיים תכונות מסויימות. השלב הבא במתמטיקה הוא לרוב לבדוק אילו <strong>מניפולציות</strong> אפשר להפעיל על האובייקט הזה שעדיין מותירות את הסדר הפנימי בו על כנו במובן מסויים. באלגברה לינארית המניפולציות הללו נקראות טרנספורמציות לינאריות. לפני שאתן את ההגדרה, הכי פשוט להציג את הדוגמה הקלאסית: חשבו על {% equation %}\mathbb{R}^{3}{% endequation %}, עליו ניתן לחשוב גם פשוט בתור המרחב האוקלידי התלת-ממדי הרגיל. מניפולציות שאפשר לעשות על המרחב הזה הן סיבוב בזווית כלשהי סביב ציר, שיקוף ביחס לציר כלשהו, ניפוח או כיווץ של המרחב, והזזה. אני מדבר על מניפולציות על כל המרחב, אבל הן מן הסתם ישפיעו באותו האופן גם על תת-קבוצה שלו, כך שאם יש לנו במרחב רק דגם של בית, ואנחנו מסובבים את כל המרחב, גם הדגם של הבית יסתובב בהתאם. זה מה שקורה בתוכנות גרפיקה תלת-ממדיות: עובדים עם איזו גרסה סופית של {% equation %}\mathbb{R}^{3}{% endequation %} ומפעילים עליה בדיוק את הטרנספורמציות שתיארתי לעיל. עם זאת, כמובן שבפועל המצב קצת יותר בעייתי - נראה בהמשך הפוסט שהזזה היא לא באמת טרנספורמציה לינארית על פי ההגדרה שלנו.

אם כן, מהי טרנספורמציה לינארית? בראש ובראשונה זוהי פונקציה: פונקציה {% equation %}f{% endequation %} מקבוצה {% equation %}A{% endequation %} אל קבוצה {% equation %}B{% endequation %} (מה שמסומן לרוב ב-{% equation %}f:A\to B{% endequation %}) היא התאמה שלכל איבר ב-{% equation %}A{% endequation %} (שנקרא <strong>התחום</strong> של הפונקציה) מחזירה איבר ב-{% equation %}B{% endequation %} (שנקרא <strong>הטווח</strong> של הפונקציה). למשל, הפונקציה {% equation %}f:\mathbb{R}\to\mathbb{R}{% endequation %} שמוגדרת על ידי הכלל {% equation %}f\left(x\right)=x^{2}{% endequation %}, כלומר היא מעלה בריבוע את המספר שהיא מופעלת עליו. מכיוון שריבוע של מספר ממשי הוא תמיד אי שלילי, אפשר היה לכתוב אותה גם כ-{% equation %}f:\mathbb{R}\to\mathbb{R}^{+}{% endequation %} כאשר {% equation %}\mathbb{R}^{+}{% endequation %} מתאר רק את הממשיים האי שליליים.

הדוגמה הזו מצביעה על כך שהטווח של פונקציה הוא מושג "גמיש" - הוא יכול להיות קבוצה שכוללת גם איברים שהפונקציה כלל לא מעבירה אליהם אף איבר של התחום. הקבוצה של כל האיברים בטווח שאכן מופיעים כפלט של הפונקציה עבור קלט כלשהו מהתחום נקראת <strong>התמונה</strong> של הפונקציה ומסומנת לרוב בתור {% equation %}\mbox{Im}f{% endequation %} ({% equation %}\mbox{Im}{% endequation %} מלשון Image). אם הטווח של פונקציה שווה לתמונה שלה אומרים שהפונקציה היא <strong>על</strong>. כלומר, {% equation %}f\left(x\right)=x^{2}{% endequation %} היא על אם חושבים עליה כפונקציה {% equation %}f:\mathbb{R}\to\mathbb{R}^{+}{% endequation %}, אבל היא לא על אם חושבים עליה כפונקציה {% equation %}f:\mathbb{R}\to\mathbb{R}{% endequation %}. קצת מבלבל, אני יודע.

בואו נראה עוד דוגמה: {% equation %}f:\mathbb{R}^{2}\to\mathbb{R}^{2}{% endequation %} שמוגדרת על ידי {% equation %}f\left(\left(x,y\right)\right)=\left(x,-y\right){% endequation %} היא פונקציה שלכל נקודה ב-{% equation %}\mathbb{R}^{2}{% endequation %} מחזירה את השיקוף שלה ביחס לציר {% equation %}x{% endequation %}. הפונקציה הזו היא די בבירור על (נסו להוכיח זאת לעצמכם). עוד דוגמה היא הפונקציה {% equation %}f:\mathbb{R}\to\mathbb{N}{% endequation %} שמוגדרת על ידי {% equation %}f\left(x\right)=\left[\left|x\right|\right]{% endequation %} - לוקחים את הערך המוחלט של {% equation %}x{% endequation %} (עבור ממשיים זה פשוט {% equation %}x{% endequation %} בלי סימן המינוס אם היה כזה), ואז לוקחים את הערך השלם של התוצאה - המספר השלם הקרוב ביותר ל-{% equation %}\left|x\right|{% endequation %}. הסיבה שאני מביא את הפונקציה הזו היא כדי להמחיש שהתחום והטווח יכולים להיות שונים.

עם זאת, גם הדוגמה שלמעלה לא מבהירה <strong>עד כמה</strong> התחום והטווח יכולים להיות שונים, כי הטבעיים הם בכל זאת תת קבוצה של הממשיים. אז בואו נחשוב על פונקציית הגימטריה: פונקציה שלוקחת מילה (רצף סופי של תווים מהא"ב העברי) ומחזירה מספר שהוא הערך הגימטרי שלו. כאן התחום הוא "קבוצת כל המחרוזות הסופיות עם תווים בעברית" והטווח הוא {% equation %}\mathbb{N}{% endequation %}. הסיבה שאני מדגיש שהתחום והטווח יכולים להיות שונים באופיים היא שעוד מעט נדבר בדיוק על טרנספורמציות לינאריות בין מרחבים וקטוריים שונים באופיים, לכאורה.

הפונקציות שהצגתי עד כה היו "חופשיות" למדי באופיין - לא באמת דרשתי מהן דרישות אלא רק אמרתי מה הן עושות. טרנספורמציה לינארית היא פונקציה {% equation %}T:V\to W{% endequation %} (השימוש ב-{% equation %}T,S{% endequation %} וכדומה עבור טרנספורמציות לינאריות הוא סטנדרטי) עם הדרישות הנוספות ש-{% equation %}V,W{% endequation %} יהיו שניהם מרחבים וקטוריים מעל אותו שדה {% equation %}\mathbb{F}{% endequation %}, וש-{% equation %}T{% endequation %} "תכבד" את הפעולות של {% equation %}V,W{% endequation %}. פורמלית זה אומר שצריך להתקיים:
<ol>
	<li> {% equation %}T\left(v+u\right)=T\left(v\right)+T\left(u\right){% endequation %} לכל {% equation %}v,u\in V{% endequation %}.</li>
	<li> {% equation %}T\left(\lambda v\right)=\lambda T\left(v\right){% endequation %} לכל {% equation %}v\in V{% endequation %} ו-{% equation %}\lambda\in\mathbb{F}{% endequation %}.</li>
</ol>
מה קורה כאן? התנאי הראשון, בניסוח מילולי, אומר "נניח שיש לך שני איברים ב-{% equation %}V{% endequation %}: זה לא משנה אם קודם תחבר אותם ואז תפעיל את {% equation %}T{% endequation %} על התוצאה, או אם קודם תפעיל את {% equation %}T{% endequation %} עליהם בנפרד ואז תחבר את התוצאות", והתנאי השני אומר "נניח שיש לך איבר ב-{% equation %}V{% endequation %}: זה לא משנה אם קודם תכפול אותו בסקלר ואז תפעיל את {% equation %}T{% endequation %} על התוצאה או אם קודם תפעיל את {% equation %}T{% endequation %} עליו ואז תכפול את התוצאה באותו סקלר". במובן מסויים זה אומר ש-{% equation %}T{% endequation %} <strong>מתחלפת</strong> עם הפעולות של חיבור ושל כפל בסקלר.

בואו נראה דוגמה פשוטה - ראינו כבר כי המרחב {% equation %}\mathbb{R}_{2}\left[x\right]{% endequation %} של פולינומים ממעלה קטנה מ-2 עם מקדמים ממשיים "נראה כמו" המרחב {% equation %}\mathbb{R}^{2}{% endequation %}, וכעת אפשר לתת לכך משמעות מדוייקת: נגדיר טרנספורמציה {% equation %}T:\mathbb{R}_{2}\left[x\right]\to\mathbb{R}^{2}{% endequation %} שמוגדרת על ידי {% equation %}T\left(ax+b\right)=\left(a,b\right){% endequation %}, ולא קשה לראות שתכונות 1 ו-2 אכן מתקיימות על ידה. אמרתי בשעתו ש-{% equation %}T{% endequation %} היא לא יותר מאשר "לשנות את הסימון" - במקום לסמן איבר ב-{% equation %}ax+b{% endequation %} אני מסמן אותו ב-{% equation %}\left(a,b\right){% endequation %}, אבל המהות נותרת זהה: חיבור שני פולינומים וחיבור שני וקטורים ב-{% equation %}\mathbb{R}^{2}{% endequation %} זה אותו הדבר, וזה נובע מכך ש-{% equation %}T{% endequation %} מכבד את פעולת החיבור.

ועכשיו בואו נראה למה "הזזה" אינה טרנספורמציה לינארית: הזזה לדוגמה היא פונקציה {% equation %}f:\mathbb{R}^{2}\to\mathbb{R}^{2}{% endequation %} שמוגדרת על ידי {% equation %}f\left(\left(a,b\right)\right)=\left(a+2,b\right){% endequation %}. כלומר, אנחנו מזיזים ב-2 יחידות בכיוון החיובי של ציר {% equation %}x{% endequation %}. חיש קל רואים איך הכל מתרסק: {% equation %}f\left(0\cdot\left(0,0\right)\right)=\left(2,0\right){% endequation %}, אבל {% equation %}0\cdot f\left(\left(0,0\right)\right)=0{% endequation %}, כך שהזזה לא מקיימת את תכונה 2 (ואם נטרח לבדוק נראה שגם תכונה 1 לא מתקיימת). יש מובן כלשהו שבו הזזה היא "כמעט" טרנספורמציה לינארית אבל לא ניכנס אליו כעת.

בדוגמה שנתתי למעלה עם הפולינומים יש עוד שתי תכונות חשובות ש-{% equation %}T{% endequation %} מקיימת: היא על, והיא גם חד-חד ערכית (חח"ע). חד-חד ערכית פירושו ש-{% equation %}T{% endequation %} מעבירה קלטים שונים לפלטים שונים: אין שני קלטים של {% equation %}T{% endequation %} שנותנים את אותו הפלט. שתי התכונות הללו מבטיחות שניתן יהיה <strong>להפוך</strong> את {% equation %}T{% endequation %}: שקיימת טרנספורמציה {% equation %}T^{-1}:\mathbb{R}^{2}\to\mathbb{R}_{2}\left[x\right]{% endequation %} שמבצעת בדיוק את הפעולה ההפוכה לפעולת {% equation %}T{% endequation %}. במקרה שלנו הטרנספורמציה הזו היא פשוט {% equation %}T^{-1}\left(\left(a,b\right)\right)=ax+b{% endequation %}. טרנספורמציה לינארית שהיא גם הפיכה נקראת <strong>איזומורפיזם</strong> של התחום והטווח שלה: היא מעידה על כך שהתחום והטווח הם בעצם אותו מרחב וקטורי <strong>עד כדי הסימונים</strong> שאנו משתמשים בהם.

בואו נראה למה התכונות של על וחח"ע כל כך חשובות לנו כאן. נתבונן בטרנספורמציה {% equation %}T:\mathbb{R}^{2}\to\mathbb{R}^{3}{% endequation %} שמוגדרת על ידי {% equation %}T\left(\left(a,b\right)\right)=\left(a,b,0\right){% endequation %}. לא קשה לראות שתכונות 1+2 מתקיימות (ומכאן ואילך אפסיק לומר את זה; אם אני נותן טרנספורמציה בלי נימוק, תוכיחו לעצמכם שהיא אכן טרנספורמציה) והיא גם חח"ע, אבל אינה על, כי את {% equation %}\left(0,0,1\right){% endequation %} אי אפשר לקבל, למשל, ולכן גם אין לנו מושג לאן להעביר אותו אם נרצה להגדיר טרנספורמציה הפוכה ל-{% equation %}T{% endequation %}. התחושה היא שב-{% equation %}\mathbb{R}^{3}{% endequation %} יש "יותר אינפורמציה" או "יותר חופש" מאשר ב-{% equation %}\mathbb{R}^{2}{% endequation %}, אם כי עדיין לא הגענו לשלב שבו אפשר לנסח במדויק מה הולך כאן (טוב, בעצם אפשר - המימד של {% equation %}\mathbb{R}^{3}{% endequation %} גדול מהמימד של {% equation %}\mathbb{R}^{2}{% endequation %} ועוד מעט נראה שאיזומורפיזם משמר מימד).

בכיוון השני, הנה טרנספורמציה אחרת, {% equation %}T:\mathbb{R}^{3}\to\mathbb{R}^{2}{% endequation %} שמוגדרת על ידי {% equation %}T\left(\left(a,b,c\right)\right)=\left(a,b\right){% endequation %}. כאן אנחנו פשוט מוחקים את הקואורדינטה השלישית; זה גורר מייד שהטרנספורמציה אינה חח"ע כי למשל {% equation %}T\left(\left(0,0,0\right)\right)=T\left(\left(0,0,1\right)\right)=\left(0,0\right){% endequation %}. העובדה ש-{% equation %}T{% endequation %} אינה חח"ע אומרת שאנחנו "מאבדים מידע" כשאנו מפעילים אותה; והיא אינה הפיכה כי הפעם אין לנו מושג לאן להעביר את {% equation %}\left(0,0\right){% endequation %} כי יש לנו <strong>יותר מדי</strong> אפשרויות ולא ברור במי מהן לבחור (אם נבחר שרירותית להעביר את {% equation %}\left(0,0\right){% endequation %} אל {% equation %}\left(0,0,0\right){% endequation %} אז נקבל שאם מפעילים את {% equation %}T{% endequation %} על {% equation %}\left(0,0,1\right){% endequation %} ואז מפעילים את ה"הופכית" על התוצאה, מקבלים את {% equation %}\left(0,0,0\right){% endequation %}, כלומר לא חזרנו לאיבר שממנו התחלנו).

כל הדיון עד כה היה כללי למדי - במתמטיקה לעתים קרובות מגדירים פונקציה בין שני מבנים ומתעניינים בשאלה אם היא חח"ע ועל. כעת אפשר להכניס לתמונה תוצאה יפהפיה שהיא כולה אלגברה לינארית וקושרת בין "כמה הטרנספורמציה רחוקה מלהיות חח"ע" ובין "כמה הטרנספורמציה היא על".

לצורך כך, הגדרות: {% equation %}T{% endequation %} תהיה טרנספורמציה לינארית {% equation %}T:V\to W{% endequation %}. נגדיר את התמונה שלה להיות{% equation %}\mbox{Im}T=\left\{ T\left(x\right)|x\in V\right\} {% endequation %} (כבר הזכרתי זאת), ונגדיר את ה<strong>גרעין</strong> שלה להיות כל האיברים של {% equation %}V{% endequation %} שהולכים לאפס (לאיבר האפס של {% equation %}W{% endequation %}), {% equation %}\ker T=\left\{ x\in V|T\left(x\right)=0\right\} {% endequation %}. שימו לב ש-{% equation %}\mbox{Im}T{% endequation %} היא תת-קבוצה של {% equation %}W{% endequation %} בעוד {% equation %}\ker T{% endequation %} היא תת-קבוצה של {% equation %}V{% endequation %}, ויותר מכך: שתיהן הן <strong>תתי-מרחבים</strong> של המרחבים שמכילים אותן (גם כאן ההוכחה פשוטה ואותיר אותה לכם). אם הן תתי-מרחבים, אז יש להן מימד, והמשפט אומר בפשטות שאם {% equation %}V{% endequation %} הוא מרחב סוף-ממדי אז מתקיים הקשר הבא:

{% equation %}\dim V=\dim\mbox{Im}T+\dim\ker T{% endequation %}

כלומר, המימד של התחום {% equation %}V{% endequation %} שווה לסכום ממדי התמונה והגרעין של {% equation %}T{% endequation %}, לכל טרנספורמציה לינארית {% equation %}T{% endequation %} ש-{% equation %}V{% endequation %} הוא התחום שלה. אפשר ואולי גם כדאי לחשוב על כך באופן הזה: {% equation %}\dim V{% endequation %} הוא כמות המידע (או חופש) שיש במרחב שמתחילים בו, {% equation %}V{% endequation %}. {% equation %}\dim\ker T{% endequation %} הוא כמות המידע ש"הולך לאיבוד" (חשבו על 0 בתור פח זבל שכזה - תכף יתברר למה), ואחרי שזרקנו חלק מהמידע לזבל {% equation %}\dim\mbox{Im}T{% endequation %} מתאר את כמות המידע שנותר לנו בתמונה. זה הסבר בנפנוף ידיים; כאן ההוכחה היא אחד מהמקרים שבהם מה שנראה אולי מסובך במבט ראשון הופך לטריוויאלי ומובן מאליו. אבל לפני שנוכיח, בואו נבין טרנספורמציות לינאריות קצת יותר טוב.

ראשית, בואו נשכנע אתכם שהגרעין של {% equation %}T{% endequation %} מודד במובן מסויים כמה {% equation %}T{% endequation %} רחוקה מלהיות חח"ע. אם {% equation %}u,v{% endequation %} הם שני וקטורים ששוברים את החח"ע של {% equation %}T{% endequation %} אז מתקיים {% equation %}T\left(u\right)=T\left(v\right){% endequation %}. נעביר אגפים ונקבל {% equation %}T\left(u\right)-T\left(v\right)=0{% endequation %}, ובגלל ש-{% equation %}T{% endequation %} היא טרנספורמציה לינארית קיבלנו ש-{% equation %}T\left(u-v\right)=0{% endequation %}, כלומר {% equation %}u-v{% endequation %} הוא איבר בגרעין של {% equation %}T{% endequation %}. אם "נקפיא" את {% equation %}u{% endequation %} נקבל שקבוצת <strong>כל</strong> ה-{% equation %}v{% endequation %}-ים כך ש-{% equation %}T\left(u\right)=T\left(v\right){% endequation %} היא בדיוק הקבוצה {% equation %}\left\{ u+k|k\in\ker T\right\} {% endequation %}, כלומר היא בדיוק "הזזה" של הגרעין של {% equation %}T{% endequation %} על ידי חיבור {% equation %}u{% endequation %} אליו. בגלל ש-{% equation %}u{% endequation %} היה וקטור שרירותי לחלוטין, התוצאה מתקיימת לכל איבר במרחב {% equation %}V{% endequation %}. מכאן שהחח"ע של {% equation %}T{% endequation %} מופרת <strong>בדיוק באותו האופן</strong> לכל איבר במרחב, והגרעין של {% equation %}T{% endequation %} מתאר בדיוק את האופן הזה.

לחלקכם הדיון הזה עשוי להישמע מוכר באופן חשוד, ולא במקרה - זה בדיוק מה שדיברנו עליו כשאמרתי שפתרון למערכת משוואות כלשהי ניתן באמצעות חיבור של פתרון פרטי כלשהו של המערכת עם הפתרונות של המשוואה ההומוגנית. עכשיו כבר אפשר לגלות שאם {% equation %}A{% endequation %} היא מטריצה מסדר {% equation %}n\times m{% endequation %} מעל {% equation %}\mathbb{F}{% endequation %} אז היא בפרט מגדירה טרנספורמציה לינארית {% equation %}T_{A}:\mathbb{F}^{m}\to\mathbb{F}^{n}{% endequation %} על ידי {% equation %}T_{A}\left(v\right)=A\cdot v{% endequation %}, ו"מרחב הפתרונות של המשוואה ההומוגנית המוגדרת על ידי {% equation %}A{% endequation %}" הוא בדיוק "הגרעין של {% equation %}T_{A}{% endequation %}". העובדה הזו תהיה חשובה למדי בהמשך.

עכשיו הגענו לנקודה שבה אפשר לחבר את מושג הבסיס שעליו דיברנו בפוסט הקודם לטרנספורמציות לינאריות. הפאנץ' הוא שאם יש לנו בסיס {% equation %}\left\{ v_{1},\dots,v_{n}\right\} {% endequation %} למרחב {% equation %}V{% endequation %}, אז כדי לדעת איך טרנספורמציה {% equation %}T:V\to W{% endequation %} פועלת על המרחב כולו מספיק לנו לדעת איך היא פועלת על איברי הבסיס ותו לא. הנימוק פשוט, כמעט טריוויאלי: אם {% equation %}v\in V{% endequation %} הוא איבר כלשהו במרחב, אז קיימת לו הצגה <strong>יחידה</strong> כצירוף לינארי של אברי הבסיס, {% equation %}v=\sum\lambda_{i}v_{i}{% endequation %}. מתכונות הטרנספורמציה הלינארית נקבל ש-{% equation %}T\left(v\right)=T\left(\sum\lambda_{i}v_{i}\right)=\sum T\left(\lambda_{i}v_{i}\right)=\sum\lambda_{i}T\left(v_{i}\right){% endequation %}. כלומר, מספיק לדעת את {% equation %}T\left(v_{1}\right),\dots,T\left(v_{n}\right){% endequation %}, ואז התמונה של איבר ב-{% equation %}V{% endequation %} היא צירוף לינארי עם אותם מקדמים שמגדירים את האיבר ב-{% equation %}v{% endequation %}, רק שהצירוף הלינארי שמגדיר את התמונה הוא לא על אברי הבסיס אלא על התמונות שלהם.

בואו נראה דוגמה לא טריוויאלית. נתבונן במרחב {% equation %}\mathbb{R}^{3}\left[x\right]{% endequation %} ונגדיר עליו טרנספורמציה לינארית של <strong>גזירה</strong> {% equation %}D:\mathbb{R}^{3}\left[x\right]\to\mathbb{R}^{2}\left[x\right]{% endequation %}: מי שמכיר חדו"א יודע שהנגזרת של הפולינום {% equation %}ax^{2}+bx+c{% endequation %} היא {% equation %}2ax+b{% endequation %}. מצד שני, אפשר להגיע לנוסחה גם כך: בסיס ל-{% equation %}\mathbb{R}^{3}\left[x\right]{% endequation %} הוא הקבוצה {% equation %}\left\{ 1,x,x^{2}\right\} {% endequation %}, ואת פעולת הנגזרת על האיברים הללו קל לדעת: {% equation %}D\left(x^{2}\right)=2x{% endequation %} ו-{% equation %}D\left(x\right)=1{% endequation %} ו-{% equation %}D\left(1\right)=0{% endequation %}. כעת, {% equation %}ax^{2}+bx+c{% endequation %} הוא בעצם צירוף לינארי של שלושת אברי הבסיס, עם המקדמים {% equation %}a,b,c{% endequation %}, ולכן {% equation %}D\left(ax^{2}+bx+c\right)=aD\left(x^{2}\right)+bD\left(x\right)+cD\left(1\right)=a\cdot2x+b\cdot1+c\cdot0=2ax+b{% endequation %}.

בואו נעבור לדוגמה גאומטרית - סיבוב ב-90 מעלות עם כיוון השעון של {% equation %}\mathbb{R}^{2}{% endequation %}. לחשוב איך זה עובד עבור וקטור כללי יכול להיות כאב ראש; אבל די קל לחשוב איך זה עובד עבור שני וקטורים ספציפיים. הראשון, {% equation %}\left(1,0\right){% endequation %}, הוא אופקי לגמרי ומצביע "ימינה", ולכן אחרי סיבוב של 90 מעלות הוא יהיה אנכי לגמרי ויצביע "למטה", ולכן {% equation %}T\left(1,0\right)=\left(0,-1\right){% endequation %}; ואילו השני, {% equation %}\left(0,1\right){% endequation %}, הוא אנכי לגמרי ומצביע "למעלה", ולכן אחרי סיבוב של 90 מעלות הוא יהיה אופקי לגמרי ויצביע "ימינה", כלומר {% equation %}T\left(0,1\right)=\left(1,0\right){% endequation %}.

כעת אפשר לראות את הפעולה הכללית של {% equation %}T{% endequation %}: {% equation %}T\left(a,b\right)=aT\left(1,0\right)+bT\left(0,1\right)=\left(0,-a\right)+\left(b,0\right)=\left(b,-a\right){% endequation %}. קיבלנו את הנוסחה הכללית עבור {% equation %}T{% endequation %} באמצעות זה שידענו את פעולת {% equation %}T{% endequation %} על שני וקטורים ספציפיים (שלמרבה המזל מהווים בסיס).

כמו רוב הדברים באלגברה לינארית, גם התוצאה הזו היא דו-צדדית, ועדיין לא הצגתי את הצד המעניין. מצד אחד, זה מגניב ביותר שכל טרנספורמציה לינארית ניתנת לתיאור רק באמצעות פעולתה על אברי הבסיס; אבל מה שבאמת חזק כאן הוא ש<strong>כל</strong> פונקציה ששולחת את אברי הבסיס לתוך מרחב לינארי ניתנת להרחבה <strong>יחידה</strong> לטרנספורמציה לינארית על {% equation %}V{% endequation %}! שתי התוצאות הללו יחד בעצם מסווגות לנו את כל הטרנספורמציות הלינאריות שיכולות בכלל להתקיים מ-{% equation %}V{% endequation %} לתוך מרחב {% equation %}W{% endequation %} נתון. בואו ננסח את זה פורמלית:

אם {% equation %}V{% endequation %} הוא מרחב עם בסיס {% equation %}\left\{ v_{1},\dots,v_{n}\right\} {% endequation %}, אז <strong>לכל</strong> קבוצה {% equation %}\left\{ w_{1},\dots,w_{n}\right\} {% endequation %} של איברים במרחב {% equation %}W{% endequation %} קיימת טרנספורמציה לינארית יחידה {% equation %}T{% endequation %} כך ש-{% equation %}T\left(v_{i}\right)=w_{i}{% endequation %} לכל {% equation %}1\le i\le n{% endequation %}. הטרנספורמציה הזו מוגדרת לכל {% equation %}v\in V{% endequation %} באופן הצפוי הבא: {% equation %}v{% endequation %} ניתן לכתיבה באופן יחיד כ-{% equation %}\sum\lambda_{i}v_{i}{% endequation %} ולכן {% equation %}T\left(v\right)=\sum\lambda_{i}w_{i}{% endequation %}. כדאי לחשוב על כך כאילו התחלנו את הגדרת {% equation %}T{% endequation %} מכך שהגדרנו אותה על אברי הבסיס, ואז <strong>הרחבנו באופן לינארי</strong> את ההגדרה. זה רעיון בסיסי ומהותי במתמטיקה: מגדירים מחלקה מסויימת של פונקציות, ואז מראים שקיימת קבוצה בסיסית כלשהי במרחב כך שדי בהיכרות עם פעולת הפונקציה עליה כדי לדעת איך היא מתנהגת בכל המרחב. דוגמה בלתי קשורה בעליל מגיעה מאנליזה מרוכבת, שם פונקציה אנליטית נקבעת באופן יחיד ("המשכה אנליטית") על בסיס ערכיה על קבוצה פתוחה במרחב.

כעת אפשר להוכיח את המשפט המרכזי של הפוסט. כזכור, הוא אומר שמתקיים {% equation %}\dim V=\dim\mbox{Im}T+\dim\ker T{% endequation %}. אם כן, תהא {% equation %}T{% endequation %} טרנספורמציה לינארית {% equation %}T:V\to W{% endequation %}. כדי להבין את {% equation %}T{% endequation %} נרצה לקחת בסיס ל-{% equation %}V{% endequation %}, אבל לא סתם בסיס; נבחר את הבסיס שיהיה הכי טוב עבורנו. נתחיל מ-{% equation %}\ker T{% endequation %}: הוא תת-מרחב של {% equation %}V{% endequation %} ולכן גם לו יש בסיס {% equation %}u_{1},\dots,u_{r}{% endequation %} (כאן {% equation %}r=\dim\ker T{% endequation %}). כעת, את הבסיס הזה, שהוא קבוצה בלתי תלויה לינארית ב-{% equation %}V{% endequation %}, אפשר <strong>להשלים</strong> לבסיס {% equation %}\left\{ u_{1},\dots,u_{r},v_{1},\dots,v_{m}\right\} {% endequation %} של {% equation %}V{% endequation %}, ומתקיים הקשר {% equation %}r+m=\dim V{% endequation %} (הרי {% equation %}\dim V{% endequation %} הוא בדיוק גודל של בסיס), כלומר {% equation %}\dim V=\dim\ker T+m{% endequation %}. כל מה שנשאר לעשות, אם כן, הוא להשתכנע שמימד התמונה של {% equation %}T{% endequation %} הוא בדיוק {% equation %}m{% endequation %}. לצורך כך די להוכיח ש-{% equation %}T\left(v_{1}\right),\dots,T\left(v_{m}\right){% endequation %} מהווים בסיס לתמונה של {% equation %}T{% endequation %}.

איך מראים שקבוצה היא בסיס? צריך להראות שהיא בלתי תלויה, ושהיא פורשת. זה שהיא פורשת זה די מובן מאליו: איבר כללי בתמונה של {% equation %}T{% endequation %} הוא מהצורה {% equation %}T\left(v\right){% endequation %} כך ש-{% equation %}v\in V{% endequation %}. את אותו {% equation %}v{% endequation %} אפשר לכתוב כ-{% equation %}v=\sum_{i=1}^{r}\tau_{i}u_{i}+\sum_{j=1}^{m}\lambda_{j}v_{j}{% endequation %} (זה צירוף לינארי של אברי הבסיס, אבל אני מבדיל בין אותם אברי בסיס שהיו שייכים במקור לגרעין וכל היתר). כעת, {% equation %}T\left(u_{i}\right)=0{% endequation %} לכל ה-{% equation %}u_{i}{% endequation %}-ים ולכן {% equation %}T\left(v\right)=\sum\tau_{i}T\left(u_{i}\right)+\sum\lambda_{j}T\left(v_{j}\right)=\sum\lambda_{j}T\left(v_{j}\right){% endequation %}. במילים אחרות, {% equation %}T\left(v\right){% endequation %} הוא צירוף לינארי של {% equation %}T\left(v_{j}\right){% endequation %} בלבד; כל ה-{% equation %}u_{i}{% endequation %}-ים נזרקים לזבל. הם הולכים לאפס, שלא משפיע על התוצאה הסופית. זו הנקודה שבה האינפורמציה הולכת לאיבוד.

נשאר להראות ש-{% equation %}T\left(v_{1}\right),\dots,T\left(v_{m}\right){% endequation %} היא קבוצה בלתי תלויה, ולשם כך מספיק להראות שאם {% equation %}\sum\lambda_{j}T\left(v_{j}\right)=0{% endequation %} אז כל המקדמים הם אפס. מכיוון ש-{% equation %}\sum\lambda_{j}T\left(v_{j}\right)=T\left(\sum\lambda_{j}v_{j}\right){% endequation %}, הרי שאם {% equation %}\sum\lambda_{j}T\left(v_{j}\right)=0{% endequation %} נובע מכך ש-{% equation %}\sum\lambda_{j}v_{j}{% endequation %} הוא איבר בגרעין של {% equation %}T{% endequation %}. מצד שני, אם הוא איבר בגרעין אז יש לו גם הצגה בתור {% equation %}\sum\tau_{i}u_{i}{% endequation %}, כי ה-{% equation %}u{% endequation %}-ים הם בסיס לגרעין; ומכיוון שכל איבר ניתן להצגה <strong>יחידה</strong> כצירוף לינארי של אברי הבסיס, אז בהכרח {% equation %}\sum\lambda_{j}v_{j}{% endequation %} ו-{% equation %}\sum\tau_{i}u_{i}{% endequation %} היא אותה ההצגה. אבל בהצגה {% equation %}\sum\lambda_{j}v_{j}{% endequation %} המקדמים של ה-{% equation %}u{% endequation %}-ים הם אפס, ובהצגה {% equation %}\sum\tau_{i}u_{i}{% endequation %} המקדמים של ה-{% equation %}v{% endequation %}-ים הם אפס, ולכן כל המקדמים הם אפס, ובפרט ה-{% equation %}\lambda{% endequation %}-ים הם כאלו, כנדרש.

אפשר לתאר את ההוכחה הזו בדרך קצת יותר מובנית, על ידי הכנסת מושג חדש לתמונה. אם {% equation %}V{% endequation %} הוא מרחב וקטורי ו-{% equation %}U_{1},U_{2}{% endequation %} הם שני תת-מרחבים שלו, אפשר להגדיר תת-מרחב חדש {% equation %}U_{1}+U_{2}=\left\{ u_{1}+u_{2}|u_{1}\in U_{1},u_{2}\in U_{2}\right\} {% endequation %} - כלומר, תת-המרחב שכל איבר בו הוא סכום של איבר מ-{% equation %}U_{1}{% endequation %} ואיבר מ-{% equation %}U_{2}{% endequation %} (למה זה תת מרחב?). במקרה שבו האיבר היחיד שמשותף ל-{% equation %}U_{1}{% endequation %} ו-{% equation %}U_{2}{% endequation %} הוא 0 (מסמנים זאת {% equation %}U_{1}\cap U_{2}=\left\{ 0\right\} {% endequation %}) נהוג לסמן את {% equation %}U_{1}+U_{2}{% endequation %} בסימון {% equation %}U_{1}\oplus U_{2}{% endequation %} ולדבר על <strong>הסכום הישר</strong> של {% equation %}U_{1},U_{2}{% endequation %}. סכום ישר גם הוא מושג שחוזר על עצמו רבות במתמטיקה אך לא אביא הגדרה כללית יותר שלו כאן.

החשיבות של סכום ישר כאן היא שכל איבר של {% equation %}U_{1}\oplus U_{2}{% endequation %} ניתן להצגה <strong>יחידה</strong> (היחידות הזו צצה בכל מקום...) כסכום של איבר מ-{% equation %}u_{1}{% endequation %} ואיבר מ-{% equation %}u_{2}{% endequation %}; כדי לראות זאת, נניח ש-{% equation %}u_{1}+u_{2}=v_{1}+v_{2}{% endequation %} הן שתי הצגות שונות כסכום של אותו איבר. אז {% equation %}u_{1}-v_{1}=v_{2}-u_{2}{% endequation %}. כעת, {% equation %}U_{1}{% endequation %} הוא תת מרחב שכולל את {% equation %}u_{1},v_{1}{% endequation %} ולכן גם {% equation %}u_{1}-v_{1}{% endequation %} שייך ל-{% equation %}U_{1}{% endequation %}; בדומה, {% equation %}v_{2}-u_{2}{% endequation %} שייך ל-{% equation %}U_{2}{% endequation %}, ומכיוון שבשני המקרים מדובר על אותו איבר בדיוק, קיבלנו שהוא שייך הן ל-{% equation %}U_{1}{% endequation %} והן ל-{% equation %}U_{2}{% endequation %} ולכן הוא אפס, ולכן {% equation %}u_{1}-v_{1}=0{% endequation %} כלומר {% equation %}u_{1}=v_{1}{% endequation %} ובדומה {% equation %}u_{2}=v_{2}{% endequation %}. הנה עוד דוגמה להוכחה מקסימה שבה הכל פשוט מסתדר מעצמו.

לא קשה לראות שהמימד של {% equation %}U_{1}\oplus U_{2}{% endequation %} הוא סכום הממדים של {% equation %}U_{1}{% endequation %} ו-{% equation %}U_{2}{% endequation %}; בסיס ל-{% equation %}U_{1}\oplus U_{2}{% endequation %} יהיה פשוט איחוד של הבסיסים של {% equation %}U_{1}{% endequation %} ו-{% equation %}U_{2}{% endequation %}, והעובדה שזה בסיס נובעת בקלות מעניין ההצגה היחידה שהוכחתי למעלה.

כעת, את מה שעשיתי בהוכחה למעלה אפשר לתאר כך: כתבתי את {% equation %}V{% endequation %} בתור {% equation %}V=\ker T\oplus U{% endequation %} כאשר {% equation %}U{% endequation %}<strong> </strong>הוא תת מרחב של {% equation %}V{% endequation %}<strong> </strong>שהוא <strong>איזומורפי</strong> ל-{% equation %}\mbox{Im}T{% endequation %} (שהוא תת-מרחב של {% equation %}W{% endequation %}). עם מה שמכונה Abuse of Notation (כלומר, שימוש בסימון <strong>שגוי</strong> כדי לתאר רעיון נכון) אפשר לומר שהראיתי ש-{% equation %}V=\ker T\oplus\mbox{Im}T{% endequation %}, ולכן, ממה שאמרתי על מימד של סכום ישר, מובן מאליו מייד ש-{% equation %}\dim V=\dim\ker T+\dim\mbox{Im}T{% endequation %}; אבל כאמור, זו לא הוכחה פורמלית אלא דרך לזכור ולהבין את האינטואיציה.

בפוסט הבא נמשיך לדבר על טרנספורמציות לינאריות, כשהפעם אחתור למה שהוא כבר באמת גביע קדוש - העובדה שטרנספורמציות לינאריות ומטריצות זה בעצם אותו הדבר בדיוק.