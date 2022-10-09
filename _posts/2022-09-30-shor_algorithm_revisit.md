---
title: "חישוב קוונטי: האלגוריתם של שור"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
  - האלגוריתם של שור
  - שברים משולבים

description: "האלגוריתם של שור הוא הקלף המנצח של חישוב קוונטי: גם פותר בעיה פרקטית מעניינת, וגם עושה את זה עם המון מתמטיקה מגניבה מסוגים שונים ומשונים"
image: "2022/shor_algorithm.png"
---


<h2>מבוא</h2>

סדרת הפוסטים הקודמת שלי על חישוב קוונטי הסתיימה <a href="https://gadial.net/2014/08/24/shor_algorithm/">בפוסט גדול על האלגוריתם של שור</a>. אני חושב שהגיע הזמן לתת עוד סיבוב, עם פוסט שייתן מבט רחב יותר על מה הרעיון הכללי של האלגוריתם ואיך הוא עובד, ויוותר על חלק מהפרטים הקטנים שכבר הוכחתי בפוסט המקורי ההוא. היתרון הגדול שלי עכשיו על פני הסיבוב הקודם הוא שכבר היו לי פוסטים נפרדים על <a href="https://gadial.net/2022/09/01/quantum_fourier_transform/">התמרת פורייה הקוונטית</a> ועל <a href="https://gadial.net/2022/09/06/phase_estimation_algorithm/">אלגוריתם הערכת פאזה</a>, שהם הרכיבים הקוונטיים המרכזיים של האלגוריתם, והיכרות איתם מאפשרת להסתכל עליו "ממעוף הציפור", מה שבלתי אפשרי בלעדיהם.

אז בואו נתחיל עם מעוף הציפור הזה. ראשית, הבעיה שאלגוריתם שור בא לפתור היא בעיית <strong>הפירוק לגורמים</strong>: נתון לנו מספר טבעי {% equation %}N{% endequation %}, ואנחנו מחפשים מספר טבעי {% equation %}1<d<N{% endequation %} כך ש-{% equation %}d{% endequation %} מחלק את {% equation %}N{% endequation %}. למשל עבור {% equation %}N=15{% endequation %} אנחנו נשמח לקבל את {% equation %}d=3{% endequation %} או {% equation %}d=5{% endequation %}. זו נראית בעיה לא גדולה כל כך במספרים קטנים, אבל כש-{% equation %}N{% endequation %} הוא מספר בן מאות ספרות, אפילו האלגוריתמים המחוכמים ביותר שיש לנו כיום שאינם משתמשים במחשב קוונטי (ואלו אלגוריתמים <strong>מאוד</strong> מחוכמים, עם מתמטיקה <strong>מאוד</strong> מתקדמת) לא מסוגלים להתמודד עם הבעיה, וזה למרות שקל לנו לעשות חשבונות עם מספרים בני מאות ספרות; זו לא סתם בעיה של "המספר גדול מכדי שנעשה איתו כל דבר שהוא" - זו בעיה של <strong>סיבוכיות זמן ריצה אקספוננציאלית</strong>. מה שהאלגוריתם של שור מציע הוא פתרון <strong>מהיר</strong> של הבעיה, בזמן ריצה <strong>פולינומי</strong> (לא חייבים באמת להבין מה המילים הללו אומרות, מעבר לזה שכאן "אקספוננציאלי" זו מילה נרדפת לא מדוייקת ל"איטי" ו"פולינומי" זו מילה נרדפת לא מדוייקת ל"מהיר"). בשביל המהירות הגדולה הזו, האלגוריתם של שור משתמש במחשב קוונטי (אם כי טרם נבנה מחשב קוונטי שמסוגל להריץ את שור עבור מספרים בני מאות ספרות, וזו שאלה טובה מתי יהיה כזה).

אחרי שאמרנו את זה, צריך להבהיר שהאלגוריתם של שור, למעשה, <strong>איננו</strong> אלגוריתם לפירוק לגורמים! הוא אלגוריתם שבא לפתור בעיה אחרת, שנקראת "בעיית מציאת הסדר", כי היכולת שלנו לפתור את בעיית מציאת הסדר נותנת לנו גם שיטה לפירוק לגורמים, אבל החלק שנעזר במציאת הסדר כדי לפרק לגורמים הוא חלק "קלאסי", שלא מעורב בו חישוב קוונטי. 

עוד נקודה שצריך להבהיר היא שהאלגוריתם של שור הוא <strong>הסתברותי</strong> - ייתכן בהחלט שנריץ אותו, לא נקבל שום דבר שיעזור לנו לפרק את {% equation %}N{% endequation %} לגורמים, ונאלץ להריץ אותו שוב. ההסתברות שהוא יצליח היא טובה למדי, אבל הניתוח שנדרש כדי להראות את זה הוא לא פשוט.

ולבסוף, החלק הקוונטי של האלגוריתם של שור הוא פשוט מקרה ספציפי של אלגוריתם הערכת הפאזה, עבור {% equation %}U{% endequation %} קונקרטי כלשהו שאציג בהמשך. זה מקרה מעניין יותר ממה שדיברנו עליו בפוסט הקודם, כי שם היה נתון לנו {% equation %}\left|u\right\rangle {% endequation %} שהוא וקטור עצמי של {% equation %}U{% endequation %}, אבל באלגוריתם של שור אין לנו מושג מי הוקטורים העצמיים של {% equation %}U{% endequation %}; אבל באמצעות תעלול מחוכם ויפה, אנחנו הולכים להריץ את אלגוריתם הערכת הפאזה על <strong>סופרפוזיציה</strong> של הערכים העצמיים של {% equation %}U{% endequation %} ואיכשהו זה יסתדר לנו.

גם אחרי שאלגוריתם הערכת הפאזה הסתיים, הפלט שלו הוא לא התוצאה הסופית של שום דבר - הוא בוודאי לא מספר שמחלק את {% equation %}N{% endequation %}, אבל הוא אפילו לא אותו "סדר" מסתורי שאנחנו צריכים למצוא; מה שאלגוריתם הערכת הפאזה נותן לנו הוא מספר רציונלי בין 0 ל-1 שבפני עצמו אין בו כלום; מה שאנחנו עושים (וגם זה חישוב קלאסי לגמרי) הוא ליצור בדרך מסויימת סדרה של <strong>קירובים</strong> לתוצאה הזו של הערכת הפאזה שקיבלנו. כל קירוב כזה יהיה מספר רציונלי {% equation %}\frac{s}{r}{% endequation %}, כשהמכנה {% equation %}r{% endequation %} <strong>עשוי להיות</strong> ה"סדר" שחיפשנו. זה אומר שבהינתן התוצאה של שור, אנחנו מקבלים קבוצה של כמה וכמה מועמדים להיות ה"סדר", ועבור כל אחד מהם צריך לבדוק אם הוא איכשהו נותן לנו פירוק לגורמים של {% equation %}N{% endequation %}.

זה נשמע ממש מסורבל - איפה זה ואיפה הגרסה האוטופית המדומיינת של האלגוריתם של שור, שבה אנחנו עושים איזה מעגל קוונטי חמוד, מודדים ומקבלים גורם של {% equation %}N{% endequation %}. אבל ככה זה בחישוב קוונטי - זה אף פעם לא פשוט כמו שעושים מזה, אבל כשמבינים את הפרטים המשוגעים זה נהיה עוד יותר יפה משזה נשמע במבט ראשון.

<h2>איך "מציאת סדר" עוזרת לפרק מספר לגורמים?</h2>

בואו ניכנס קצת יותר לפרטים של מה עושים כשרוצים למצוא גורם של {% equation %}N{% endequation %}. המתמטיקה שצריך להכיר פה היא זו של <strong>חשבון מודולרי</strong>, כלומר של ביצוע פעולות חיבור וכפל כשבסוף מחלקים במשהו ולוקחים את השארית. החישובים שלנו יהיו מודולו {% equation %}N{% endequation %}. למשל, אם {% equation %}N=15{% endequation %} ו-{% equation %}a=7{% endequation %} אז {% equation %}7^{2}{% endequation %} מודולו {% equation %}N{% endequation %} הוא שארית החלוקה של 49 ב-15, כלומר 4. כותבים את זה {% equation %}7^{2}\equiv_{N}4{% endequation %}. הדבר השני שצריך להכיר הוא את הקיום של אלגוריתם יעיל שבהינתן שני מספרים {% equation %}a,b{% endequation %} מחשב את ה-{% equation %}\text{gcd}\left(a,b\right){% endequation %} - המספר הגדול ביותר שמחלק את {% equation %}a{% endequation %} וגם את {% equation %}b{% endequation %}. לא חשוב כרגע איך אלגוריתם עושה את זה (<a href="https://gadial.net/2011/09/12/euclidean_algorithm_and_rings/">יש לי פוסט</a>) אלא רק שאפשר לבדוק את זה ביעילות.

מה זה ה"סדר" המסתורי שהאלגוריתם של שור מחשב? זה המושג הסטנדרטי מתורת החבורות: הסדר של {% equation %}a{% endequation %} מודולו {% equation %}N{% endequation %} הוא המספר {% equation %}r>0{% endequation %} המינימלי שעבורו {% equation %}a^{r}\equiv_{N}1{% endequation %}. מספר כזה קיים בהכרח רק {% equation %}\text{gcd}\left(a,N\right)=1{% endequation %}; אבל אם {% equation %}\text{gcd}\left(a,N\right)>1{% endequation %} אז המספר {% equation %}\text{gcd}\left(a,N\right){% endequation %} (שאפשר לחשב ביעילות, כאמור) הוא מחלק לא טריוויאלי של {% equation %}N{% endequation %} וסיימנו.

אז איך עובד כל התהליך? ראשית, בודקים ש-{% equation %}N{% endequation %} הוא לא זוגי, כלומר פשוט מנסים לחלק אותו ב-2. אם כן - סיימנו. אחרת, בודקים ש-{% equation %}N{% endequation %} הוא לא חזקה של ראשוני, כלומר {% equation %}N=p^{n}{% endequation %} עבור {% equation %}n{% endequation %} כלשהו. זה כבר עניין טריקי יותר, אבל יש אלגוריתם יעיל שעושה את זה ואני לא מציג אותו כי זה לא באמת קשור לאלגוריתם של שור. 

בהינתן ש-{% equation %}N{% endequation %} הוא לא מהצורה הזו, אנחנו עושים את הדבר הבא: מגרילים מספר {% equation %}1<a<N{% endequation %}. בודקים ש-{% equation %}\text{gcd}\left(a,N\right)=1{% endequation %}, כי אם הוא גדול יותר אז מצאנו מחלק של {% equation %}N{% endequation %}.

אחר כך אנחנו מפעילים את החלק הקוונטי של האלגוריתם של שור ומקבלים כל מני מספרים שכל אחד מהם הוא בעל פוטנציאל להיות הסדר של {% equation %}a{% endequation %}. לכל מספר {% equation %}r{% endequation %} כזה, אם {% equation %}r{% endequation %} אי זוגי מתעלמים ממנו, ואם {% equation %}r{% endequation %} זוגי, אנו בודקים האם {% equation %}\text{gcd}\left(a^{\frac{r}{2}}-1,N\right)>1{% endequation %} או ש-{% equation %}\text{gcd}\left(a^{\frac{r}{2}}+1,N\right)>1{% endequation %}. אם קיבלנו מספר כזה, סיימנו; מצאנו מחלק לא טריוויאלי של {% equation %}N{% endequation %}. אם לכל ה-{% equation %}r{% endequation %}-ים שעשינו הניסוי לא הצליח, אנחנו מגרילים {% equation %}a{% endequation %} אחר ומנסים שוב. זהו, זה כל האלגוריתם... למעט החלק של מציאת הסדר, שהוא כאמור העיקר.

למה כל זה עובד? כאן מגיעה הוכחה קצת מייגעת מתורת המספרים, שאני ארשה לעצמי לדלג עליה לגמרי כי כבר יש לי אותה <a href="https://gadial.net/2014/08/24/shor_algorithm/">בפוסט הקודם</a> על האלגוריתם של שור. זה עובד, תסמכו עלי. אנחנו פה בשביל החלק הקוונטי.

<h2>איך בגדול עובד אלגוריתם מציאת הסדר?</h2>

בואו ניזכר מה עושה אלגוריתם הערכת הפאזה: הוא מניח שאנחנו יודעים לבנות מעגל עבור אופרטור {% equation %}U:\mathbb{C}^{2^{m}}\to\mathbb{C}^{2^{m}}{% endequation %}, ובהינתן שני רגיסטרים קוונטיים (שזה שם יפה ל"הרבה קיוביטים שאנחנו מחלקים אותם קונספטואלית לשתי קבוצות") {% equation %}\left|0^{n}\right\rangle \left|u\right\rangle {% endequation %} כך ש-{% equation %}\left|u\right\rangle {% endequation %} הוא וקטור עצמי של {% equation %}U{% endequation %}, אנחנו מסוגלים לבצע חישוב שבסוף שלו מדידה של הרגיסטר הראשון תניב קירוב ל-{% equation %}\varphi{% endequation %}, שהוא מספר {% equation %}0\le\varphi\le1{% endequation %} שמקיים {% equation %}U\left|u\right\rangle =e^{2\pi i\varphi}{% endequation %}.

לכן, כשאנחנו באים להשתמש באלגוריתם הזה בפועל, השאלה הראשונה שאנחנו צריכים לענות עליה היא מהו {% equation %}U{% endequation %} שלנו, והשניה היא מהו {% equation %}\left|u\right\rangle {% endequation %}. בואו נראה איך זה יהיה אצלנו.

ראשית, בואו ניזכר איך אני משתמש בכתיב {% equation %}\left|a\right\rangle {% endequation %} כאשר {% equation %}a{% endequation %} הוא מספר טבעי. למשל, אם {% equation %}a=5{% endequation %} אז הייצוג הבינארי של {% equation %}a{% endequation %} הוא {% equation %}101{% endequation %}, ואז הסימון {% equation %}\left|a\right\rangle {% endequation %} מסמן את {% equation %}\left|101\right\rangle =\left|1\right\rangle \otimes\left|0\right\rangle \otimes\left|1\right\rangle {% endequation %}. צריך קצת להיזהר - אם מלכתחילה ברגיסטר שלנו משתתפים יותר קיוביטים מאשר צריך ספרות כדי לייצג את המספר, אז כל הקיוביטים ה"מיותרים" יהיו אפס. למשל, אם יש חמישה קיוביטים ואני מתבונן על המספר {% equation %}13{% endequation %}, אז {% equation %}\left|13\right\rangle =\left|01101\right\rangle {% endequation %}. מעכשיו בכל מה שהולך לקרות באלגוריתם של שור, אני אשתמש רק בסימון {% equation %}\left|a\right\rangle {% endequation %} כש-{% equation %}a{% endequation %} הוא מספר טבעי; אני לא אכתוב דברים בינאריים שם.

עכשיו אפשר לתאר את {% equation %}U{% endequation %}. כזכור, אלגוריתם מציאת הסדר מקבל כקלט מספר {% equation %}N{% endequation %} ומספר {% equation %}a<N{% endequation %} והשאלה היא מהו הסדר של {% equation %}a{% endequation %} מודולו {% equation %}N{% endequation %}. אז האופרטור {% equation %}U{% endequation %} שבו משתמשים נבנה בהתבסס על שני המספרים הללו:

{% equation %}U\left|b\right\rangle =\left|ab\text{ mod }N\right\rangle {% endequation %}

כלומר, הוא בסך הכל כפל ב-{% equation %}a{% endequation %} מודולו {% equation %}N{% endequation %}. בגלל שמעצבן לכתוב כל הזמן {% equation %}\text{mod }N{% endequation %} אני הולך להשמיט אותו מעכשיו והלאה, אבל בכל פעם שבה מופיע משהו כמו {% equation %}\left|a^{2}\right\rangle {% endequation %}, תזכרו שאני מתכוון אל הערך של {% equation %}a^{2}{% endequation %} מודולו {% equation %}N{% endequation %}.

עכשיו, אם אנחנו זוכרים, בהערכת פאזה צריך להיות מסוגלים לחשב לא רק את {% equation %}U{% endequation %} אלא גם את {% equation %}U^{2^{t}}{% endequation %} עבור ערכים הולכים וגדלים של {% equation %}t{% endequation %}, כלומר לחשב

{% equation %}U^{2^{t}}\left|b\right\rangle =\left|a^{2^{t}}b\text{ mod }N\right\rangle {% endequation %}

אני <strong>לא הולך להסביר</strong> בפוסט הזה איך עושים את זה, כדי להישאר ממוקד. יש איזו פרדוקסליות בשאלה איך עושים את זה. מצד אחד, באופן כללי אנחנו מסוגלים לבצע חישובים "רגילים" במחשב קוונטי, מה שמזמין פוסט שעומד בפני עצמו שמסביר איך בדיוק עושים את זה. מצד שני, השאלה איך מחשבים את {% equation %}U^{2^{t}}{% endequation %} בצורה אופטימלית, עם מינימום שערים, היא לא שאלה סגורה גם כיום. לכל זוג של {% equation %}a,N{% endequation %} בעצם בונים מעגל אחר שמבצע את החישוב המתאים, וזו בעיה קלאסית בתחום של <strong>סינתזה</strong> של מעגלים קוונטיים - הבניה של מעגל אופטימלי מתוך התיאור האבסטרקטי יותר שלו. אז אני לא נכנס לזה בפוסט הזה כי זה מזמין סדרת פוסטים בפני עצמה. אבל אפשר לעשות את זה.

יפה, אז יש לנו את האופרטור {% equation %}U\left|b\right\rangle =\left|ab\text{ mod }N\right\rangle {% endequation %}. איך בדיוק הוא קשור לסדר {% equation %}r{% endequation %} של {% equation %}a{% endequation %} מודולו {% equation %}N{% endequation %}? איך כל זה קשור ל"פאזה"? מה הולך כאן? בואו נפיל את האסימון הזה - לטעמי זה הולך להיות הרגע היפה ביותר מבין כל מה שראינו עד כה בסדרת הפוסטים הזו על חישוב קוונטי. כל כך יפה, שאני ארשה לעצמי להיות לא מדויק בניסוחים שלי - בהמשך גם זה יגיע.

בואו נסתכל לרגע על מה {% equation %}U{% endequation %} עושה לכמה איברים קונקרטיים:

{% equation %}U\left|1\right\rangle =\left|a\cdot1\text{ mod }N\right\rangle =\left|a\right\rangle {% endequation %}

{% equation %}U\left|a\right\rangle =\left|a\cdot a\text{ mod }N\right\rangle =\left|a^{2}\right\rangle {% endequation %}

{% equation %}U\left|a^{2}\right\rangle =\left|a\cdot a^{2}\text{ mod }N\right\rangle =\left|a^{3}\right\rangle {% endequation %}

אוקיי, אנחנו מבינים, על סדרת הערכים {% equation %}1,a,a^{2},\ldots{% endequation %} מה ש-{% equation %}U{% endequation %} עושה הוא לקדם את האיבר הנוכחי אל האיבר הבא בסדרה. אבל מתי זה נגמר? ובכן, זה נגמר בדיוק כשמגיעים לסדר של {% equation %}a{% endequation %} - לאיבר {% equation %}a^{2}\equiv_{N}1{% endequation %}. במילים אחרות:

{% equation %}U\left|a^{r-1}\right\rangle =\left|a\cdot a^{r-1}\text{ mod }N\right\rangle =\left|1\right\rangle {% endequation %}

ואז אנחנו חוזרים אל <strong>התחלת</strong> הסדרה (במתמטית אומרים על זה ש-{% equation %}U{% endequation %} מבצע לסדרה {% equation %}1,a,a^{2},\ldots,a^{r-1}{% endequation %} <strong>הזזה ציקלית</strong>).

סבבה, איך זה נותן לנו וקטור עצמי של {% equation %}U{% endequation %}? פשוט מאוד: בואו ניקח <strong>סופרפוזיציה אחידה</strong> של כל אברי הסדרה הזו, כלומר נסתכל על המצב

{% equation %}\left|u_{0}\right\rangle =\frac{\left|1\right\rangle +\left|a\right\rangle +\left|a^{2}\right\rangle +\ldots+\left|a^{r-1}\right\rangle }{\sqrt{r}}=\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\left|a^{k}\right\rangle {% endequation %}

המצב הזה הוא בבירור מצב עצמי של {% equation %}U{% endequation %}, כלומר {% equation %}U\left|u_{0}\right\rangle =\left|u_{0}\right\rangle {% endequation %}; הוא מתאים לערך העצמי 1, וזה... לא עוזר לנו... בשום צורה? אלגוריתם הערכת הפאזה, אם יופעל על המצב הזה, יחזיר לנו 0. זה לא נותן לנו את {% equation %}r{% endequation %}; זה לא נותן לנו שום כלום. אז בשביל מה אני משגע אתכם?

אה-הא! העניין הוא שיש <strong>עוד</strong> וקטורים עצמיים! {% equation %}\left|u_{0}\right\rangle {% endequation %} הוא רק האבטיפוס; הדוגמא הראשונה והפשוטה שנותנת לנו את האינטואיציה כדי להמשיך הלאה. בואו נחשוב לרגע על אותו וקטור, אבל עם <strong>מקדמים</strong> עבור האיברים:

{% equation %}\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k}\right\rangle {% endequation %}

אם אנחנו רוצים שאחרי הפעלת {% equation %}U{% endequation %} נחזור לאותו מצב בדיוק כפול סקלר כלשהו, צריך להתקיים

{% equation %}U\left(\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k}\right\rangle \right)=\lambda\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k}\right\rangle {% endequation %}

אבל

{% equation %}U\left(\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k}\right\rangle \right)=\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}U\left(\left|a^{k}\right\rangle \right)=\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k+1\text{ mod }r}\right\rangle {% endequation %}

אם אנחנו משווים את זה אל {% equation %}\lambda\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k}\right\rangle {% endequation %} אנחנו מקבלים

{% equation %}\lambda\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k}\right\rangle =\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}\alpha_{k}\left|a^{k+1\text{ mod }r}\right\rangle {% endequation %}

ואחרי חילוץ המקדמים, אנחנו מקבלים את המשוואות

{% equation %}\lambda\alpha_{0}=\alpha_{r-1}{% endequation %}

{% equation %}\lambda\alpha_{1}=\alpha_{0}{% endequation %}

{% equation %}\lambda\alpha_{2}=\alpha_{1}{% endequation %}

וכן הלאה, עד שמגיעים לבסוף אל

{% equation %}\lambda\alpha_{r-1}=\alpha_{r-2}{% endequation %}

אם נכפול את אגפי ימין ושמאל של כל המשוואות, נקבל

{% equation %}\lambda^{r}\prod_{k=0}^{r-1}\alpha_{k}=\prod_{k=0}^{r-1}\alpha_{k}{% endequation %}

כלומר, {% equation %}\lambda^{r}=1{% endequation %}. או במילים אחרות, אנחנו מסוגלים לקבל וקטור עצמי עבור כל <strong>שורש יחידה </strong>מסדר<strong> </strong>{% equation %}r{% endequation %}.

הצורה הכללית של שורש יחידה מסדר {% equation %}r{% endequation %} היא

{% equation %}e^{\frac{2\pi i}{r}\cdot s}{% endequation %}

כאשר {% equation %}0\le s<r{% endequation %}.

עכשיו, עבור שורש יחידה {% equation %}e^{\frac{2\pi i}{r}\cdot s}{% endequation %} קונקרטי, איך נקבל את הוקטורים העצמיים המתאימים? אפשר לקבוע שרירותית שתמיד יתקיים {% equation %}\alpha_{0}=1{% endequation %} כי ככה דברים ייצאו לנו נחמד, ואז נובע ש-

{% equation %}\alpha_{1}=\lambda^{-1}\alpha_{0}=e^{-\frac{2\pi i}{r}\cdot s}{% endequation %}

ובדומה נקבל

{% equation %}\alpha_{2}=e^{-2\cdot\frac{2\pi i}{r}\cdot s}{% endequation %}

ובאופן כללי, נקבל את הוקטור העצמי

{% equation %}\left|u_{s}\right\rangle =\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}e^{-k\cdot\frac{2\pi i}{r}s}\left|a^{k}\right\rangle {% endequation %}

והוקטור {% equation %}\left|u_{0}\right\rangle {% endequation %} שראינו קודם אכן מתקבל כאן כמקרה פרטי, כאשר {% equation %}s=0{% endequation %}.

האם אלו באמת וקטורים עצמיים? אפשר לעשות שוב את החישוב, אבל כבר עשינו אותו קודם והוא יעבוד באותה צורה כל פעם. עבור {% equation %}\left|u_{s}\right\rangle {% endequation %}, הערך העצמי הוא שורש היחידה ה-{% equation %}r{% endequation %}-י שהתאים ל-{% equation %}s{% endequation %}, כלומר

{% equation %}U\left|u_{s}\right\rangle =e^{\frac{2\pi i}{r}s}\left|u_{s}\right\rangle {% endequation %}

ואם לחזור ללשון של אלגוריתם הערכת הפאזה, אז הפאזה {% equation %}\varphi_{s}{% endequation %} של {% equation %}\left|u_{s}\right\rangle {% endequation %} היא {% equation %}\varphi_{s}=\frac{s}{r}{% endequation %}. בפרט, <strong>אם</strong> הייתה לנו דרך להפעיל את אלגוריתם הערכת הפאזה על {% equation %}\left|u_{1}\right\rangle {% endequation %} ולקבל תוצאה מדויקת, אז היינו מקבלים ליד את המספר הרציונלי {% equation %}\frac{1}{r}{% endequation %}. היינו מקבלים אותו בייצוג בינארי, אבל מתוך הייצוג הזה קל לחשב את {% equation %}r{% endequation %} עצמו, מה שמסיים לנו את כל העבודה!

זהו, זו "נפילת האסימון" המדוברת. זה האופן שבו הסדר {% equation %}r{% endequation %} עשוי לצוץ מתוך אלגוריתם הערכת פאזה. כשאני רוצה לסכם לעצמי את הפאנץ' של האלגוריתם, אני חושב על הסדרה {% equation %}1,a,a^{2},\ldots,a^{r-1}{% endequation %} ואומר לעצמי "הזזה ציקלית. הזזה ציקלית".

העניין הוא שזה לא מספיק. מה שתיארתי עד כה הוא אמנם נכון מבחינה רעיונית, אבל אנחנו לא באמת מסוגלים לממש את זה בפועל. נזדקק לעוד תעלול אחד אחרון. והתעלול הזה הוא כנראה הדבר הכי מגניב פה.

מה בעצם הבעיה? אם הייתי מסוגל להפעיל את אלגוריתם הערכת הפאזה על {% equation %}\left|u_{1}\right\rangle {% endequation %} אכן הייתי מקבל את {% equation %}\frac{1}{r}{% endequation %} (או לפחות קירוב טוב של {% equation %}\frac{1}{r}{% endequation %} ועוד נחזור לחישוב המדויק). אבל <strong>אני לא יודע</strong> את {% equation %}\left|u_{1}\right\rangle {% endequation %}. אין לי מושג איך לבנות אותו. המקדמים שלו מקודדים איכשהו את {% equation %}e^{\frac{2\pi i}{r}}{% endequation %}; בשביל ליצור אותם אני כנראה אצטרך לדעת מה הוא {% equation %}r{% endequation %}, שהוא המספר שאותו אנחנו מחפשים! לכאורה אני במעגל ולא התקדמתי אף צעד; זה הכי כיף כשנראה שאנחנו בסיטואציה כזו כשלמעשה אנחנו במרחק צעד אחד מהפתרון.

הפתרון הוא לקחת את <strong>כל</strong> הוקטורים העצמיים {% equation %}\left|u_{s}\right\rangle {% endequation %}, עבור <strong>כל</strong> {% equation %}0\le s<r{% endequation %}, ולהסתכל על הסופרפוזיציה של כולם ביחד, כלומר על

{% equation %}\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\left|u_{s}\right\rangle {% endequation %}

לכאורה לא התקדמנו בכלל - קודם היה מצב אחד שלא היה לנו מושג מהו, ועכשיו יש לנו סופרפוזיציה של הרבה מצבים כאלו; איך אנחנו אמורים לבנות אותה? התשובה היא שהיא מצב שאנחנו מכירים היטב וקל לנו מאוד לבנות - רק צריך לעשות את החישוב:

{% equation %}\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\left|u_{s}\right\rangle =\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\left(\frac{1}{\sqrt{r}}\sum_{k=0}^{r-1}e^{-k\cdot\frac{2\pi i}{r}s}\left|a^{k}\right\rangle \right)={% endequation %}

{% equation %}=\frac{1}{r}\sum_{k=1}^{r-1}\left(\sum_{s=0}^{r-1}e^{-k\cdot\frac{2\pi i}{r}s}\right)\left|a^{k}\right\rangle {% endequation %}

עכשיו נחלץ לעזרתנו תעלול ידוע ומוכר - אם {% equation %}\omega{% endequation %} הוא שורש יחידה <strong>כלשהו</strong> מסדר {% equation %}r{% endequation %}, אז {% equation %}1+\omega+\omega^{2}+\ldots+\omega^{r-1}=\begin{cases} 0 & \omega\ne1\\ r & \omega=1 \end{cases}{% endequation %}. למה? כי אם {% equation %}\omega\ne1{% endequation %} אז הסכום משמאל הוא טור הנדסי שיוצא {% equation %}\frac{\omega^{r}-1}{\omega-1}=\frac{1-1}{\omega-1}=0{% endequation %}.

במקרה שלנו, {% equation %}\omega=-k\frac{2\pi i}{r}{% endequation %} - זה בהחלט שורש יחידה מסדר {% equation %}r{% endequation %}, והוא שווה ל-1 רק כאשר {% equation %}k=0{% endequation %}. כלומר מכל הסכום הגדול נשאר רק

{% equation %}\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\left|u_{s}\right\rangle =\frac{1}{r}\cdot r\left|a^{0}\right\rangle =\left|1\right\rangle {% endequation %}

שימו לב: {% equation %}\left|1\right\rangle {% endequation %} במקרה הזה הוא לא קיוביט בודד שערכו {% equation %}\left|1\right\rangle {% endequation %}, אלא כזכור, הסימון המקוצר שלי ל-{% equation %}\left|000\ldots01\right\rangle {% endequation %}. אבל זה בוודאי ובוודאי מצב שאנחנו יודעים לבנות - כלומר, אנחנו בהחלט יודעים לקבל את הסופרפוזיציה של כל ה-{% equation %}\left|u_{s}\right\rangle {% endequation %} גם אם אנחנו לא יודעים לקבל אף אחד מהם אישית; זו גם הסיבה שבגללה כל כך עניין אותי להבין את כל ה-{% equation %}\left|u_{s}\right\rangle {% endequation %} כולל {% equation %}\left|u_{0}\right\rangle {% endequation %} ולא סתם התמקדתי ב-{% equation %}\left|u_{1}\right\rangle {% endequation %}.

בסופו של דבר, מה עושה המעגל של אלגוריתם הערכת פאזה? נקרא לו {% equation %}\text{PE}{% endequation %} (קיצור של Phase Estimation). אם מריצים אותו עד השלב שלפני המדידה שבסוף, הוא מחשב את האופרטור האוניטרי

{% equation %}\text{PE}\left(\left|0^{n}\right\rangle \left|u_{s}\right\rangle \right)=\left|\tilde{\varphi}_{s}\right\rangle \left|u_{s}\right\rangle {% endequation %}

כאשר {% equation %}\left|\tilde{\varphi}_{s}\right\rangle {% endequation %} הוא מצב קוונטי שהמדידה שלו נותנת בהסתברות טובה קירוב טוב של {% equation %}\varphi_{s}{% endequation %} - הפאזה שמתאימה ל-{% equation %}u_{s}{% endequation %}, כלומר {% equation %}\frac{s}{r}{% endequation %}. עכשיו, אם במקום לרוץ על מצב בודד, נרוץ על סופרפוזיציה שלהם, העובדה ש-{% equation %}\text{PE}{% endequation %} הוא אופרטור <strong>לינארי</strong> נותנת לנו

{% equation %}\text{PE}\left(\left|0^{n}\right\rangle \left(\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\left|u_{s}\right\rangle \right)\right)=\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\text{PE}\left(\left|0^{n}\right\rangle \left|u_{s}\right\rangle \right)=\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1}\left|\tilde{\varphi}_{s}\right\rangle \left|u_{s}\right\rangle {% endequation %}

במילים אחרות, אנחנו מקבלים ברגיסטר הראשון סופרפוזיציה אחידה של כל ה-{% equation %}\left|\tilde{\varphi}_{s}\right\rangle {% endequation %}-ים, ולכן אפשר לחשוב על מדידה של הרגיסטר הראשון כאילו היא עושה שני דברים בזה אחר זה:

<ul> <li>מגרילה {% equation %}0\le s<r{% endequation %} באקראי ובהתפלגות אחידה.</li>


<li>מודדת את {% equation %}\left|\tilde{\varphi}_{s}\right\rangle {% endequation %}, כלומר מקבלת ערך שבהסתברות טובה הוא קירוב טוב של {% equation %}\frac{s}{r}{% endequation %}.</li>

</ul>

האם כל ה-{% equation %}s{% endequation %}-ים טובים עבורנו? ובכן, לא. ראינו כבר קודם שעבור {% equation %}s=0{% endequation %} אין לנו כלום - לא נוכל לחלץ את {% equation %}r{% endequation %} מהערך שנקבל. ובמקרים אחרים, אם {% equation %}\text{gcd}\left(s,r\right)>1{% endequation %} אז הסיכוי שנצליח לעשות משהו טוב נפגע מאוד - {% equation %}\frac{s}{r}{% endequation %} לא יהיה שבר מצומצם ולכן אם ננסה "לשחזר" את {% equation %}\frac{s}{r}{% endequation %} לא נקבל את {% equation %}r{% endequation %}. הנה דוגמא פשוטה: נניח ש-{% equation %}r=15{% endequation %} ו-{% equation %}s=3{% endequation %}. אז {% equation %}\frac{s}{r}=\frac{3}{15}=\frac{1}{5}=0.2{% endequation %}; אז אפילו אם נקבל את התוצאה המדויקת {% equation %}0.2{% endequation %} לא נוכל לשחזר מזה את {% equation %}r=15{% endequation %}; המכנה שנשחזר הוא 5. בגלל הבעיה הזו, לפעמים באלגוריתם של שור כשמקבלים "מועמד ל-{% equation %}r{% endequation %}" משתלם לפעול לא רק מתוך הנחה שהמועמד הזה טוב, אלא גם לנסות כמה כפולות שלו - להכפיל ב-2,3,4 וכו' ולנסות גם עבורן. זה חישוב מהיר מאוד שלא מאט אותנו, ואם במקרה הוא מצליח ומצאנו גורם של {% equation %}N{% endequation %} נדע בודאות שהצלחנו, כך שאין חיסרון של ממש להרחבה הזו.

זה סוף אלגוריתם הערכת הפאזה, כלומר סוף החלק הקוונטי של האלגוריתם; הנה איך הכל נראה בסופו של דבר.

<img src="{{site.baseurl}}{{site.post_images}}/2022/shor_algorithm.png" alt=""/>

<h2>איך משחזרים את הסדר מתוך הקירוב שהערכת הפאזה נותנת לנו?</h2>

ברגע שבו אלגוריתם הערכת הפאזה מסתיים, נגמר החלק הקוונטי של האלגוריתם, אבל עדיין נשאר חלק לא טריוויאלי בעליל שצריך לבצע - השלב שבו אנחנו עוברים מה<strong>קירוב</strong> שקיבלנו לפאזה, עד שיש לנו ביד מועמד פוטנציאלי להיות הסדר, {% equation %}r{% endequation %}. כאן נכנס לתמונה מה שנקרא <strong>אלגוריתם השברים המשולבים</strong>, שזו פשוט דרך מפחידה להגיד "שיטה למציאת קירובים רציונלים טובים למספר שקיבלנו".

מה זה שבר משולב? <a href="https://gadial.net/2010/05/29/continued_fractions_1/">יש לי פוסט על זה</a> אבל הוא נכנס לעומק שאני לא זקוק לו פה, ומצד שני תמיד נחמד להציג שוב נושא כל כך מגניב, בטח כשיש לו שימוש פרקטי. אז הנה מבוא על רגל אחת. נתחיל עם דוגמא קונקרטית - המספר {% equation %}\pi{% endequation %} - היחס בין היקף מעגל לקוטרו - הוא אחד מהקבועים המתמטיים המפורסמים ביותר. אם ננסה לכתוב אותו בבסיס עשרוני הוא ייראה משהו כמו {% equation %}\pi=3.14159\ldots{% endequation %}, כשהנקודות אומרות שיש עוד ספרות בהמשך. אם נוותר על הנקודות ונסתכל על המספר {% equation %}3.14159{% endequation %}, מה שיש לנו ביד הוא <strong>קירוב רציונלי</strong> של {% equation %}\pi{% endequation %} - קירוב שאפשר לכתוב אותו בתור מנה של שני מספרים שלמים, {% equation %}\frac{314159}{10000}{% endequation %} (זאת להבדיל מ-{% equation %}\pi{% endequation %} עצמו שיש הוכחה שאי אפשר להציג בתור מנה של שני מספרים שלמים). אני יכול גם להסתכל על קירובים שמתקבלים מלקחת <strong>פחות</strong> ספרות של {% equation %}\pi{% endequation %}: אני מקבל את סדרת הקירובים

{% equation %}3,\frac{31}{10},\frac{314}{100},\frac{3141}{1000},\frac{31415}{10000}{% endequation %}

האם זו סדרת קירובים <strong>טובה</strong>? הקירוב {% equation %}\frac{314}{100}=3.14{% endequation %}, למשל, הוא מפורסם במיוחד: צורת הכתיב שלו, בשילוב עם שיטת כתיב התאריכים האמריקאית ויום ההולדת של אלברט איינשטיין, הולידו את <strong>יום פאי</strong>. אבל האמת היא, בינינו, שזה קירוב <strong>די גרוע</strong> לעומת קירוב אחר, {% equation %}\frac{22}{7}{% endequation %}, שזכה ליום פחות מפורסם משל עצמו ("יום קירוב פאי", למרות שכאמור הוא דווקא הקירוב הטוב יותר). אם נחשב את ההפרש של כל אחד מהקירובים מפאי נקבל{% equation %}\left|\pi-3.14\right|=0.001592\dots{% endequation %} ו-{% equation %}\left|\pi-\frac{22}{7}\right|=0.001264\ldots{% endequation %}, כלומר יש יתרון ברור ל-{% equation %}\frac{22}{7}{% endequation %}, למרות שלכאורה נקודת המוצא של {% equation %}\frac{314}{100}{% endequation %} היא טובה <strong>הרבה </strong>יותר, כי המכנה שלו הוא מספר גדול יותר, ולכן לכאורה מאפשר למצוא מספר שקרוב לפאי ברזולוציה טובה יותר (תחשבו על סרגל שיש בו סימוני סנטימטרים לעומת סרגל שיש בו רק שבעה סימנים ברווחים אחידים בין כל מטר - מה נראה לנו כמו כלי מדויק יותר?)

אם נסתכל על הקירוב ה"טוב", {% equation %}\frac{22}{7}{% endequation %}, מה מבדיל אותו מהסדרה שהראיתי קודם? בסדרה הזו, <strong>המכנה</strong> של כל השברים היה חזקה של 10: 1, 10, 100, 1000 וכו'. לעומת בקירוב {% equation %}\frac{22}{7}{% endequation %} נדחף לנו ה-7 הלא קשור הזה. העניין הוא שמבחינת המתמטיקה, האהבה שלנו למספר 10 היא <strong>שרירותית</strong>; זה בגלל שהביולוגיה חננה אותנו בעשר אצבעות, לא בגלל שעשר הוא מספר מופלא לקירובים. לכן, שיטת הקירובים שאנחנו רגילים אליה מהבסיס העשרוני שלנו היא לאו דווקא אופטימלית; שברים משולבים הם אלו שנותנים לנו את הקירובים האופטימליים, במובן מאוד מדויק שאתאר עוד מעט - ובגלל שמקבלים קירובים כל כך טובים, זה מתקשר ישירות לאלגוריתם שלנו. 

איך זה קשור? ובכן, עוד מעט אראה איך בעזרת שברים משולבים אפשר לקבל סדרת קירובים למספר כלשהו {% equation %}x{% endequation %}. הקסם המופלא בשיטה הזו הוא שאם למספר {% equation %}x{% endequation %} כלשהו יש קירוב <strong>טוב</strong> (עבור משמעות של "טוב" שאתן במדויק בהמשך), אז <strong>בודאות מוחלטת</strong> הקירוב הטוב הזה יופיע בסדרת הקירובים שמקבלים מהפיתוח של {% equation %}x{% endequation %} לשבר משולב.

איך זה קשור אלינו? כי בואו נחשוב רגע מה עושה שלב הערכת הפאזה: הוא מחזיר מספר {% equation %}x{% endequation %} שהוא <strong>קירוב טוב</strong> של {% equation %}\frac{s}{r}{% endequation %} כאשר {% equation %}r{% endequation %} הוא הסדר שאנחנו מחפשים - מטרת האלגוריתם - ו-{% equation %}0\le s<r{% endequation %} הוא מספר אקראי. אבל אם {% equation %}x{% endequation %} הוא <strong>קירוב טוב</strong> של {% equation %}\frac{s}{r}{% endequation %} ההפך נכון באותה מידה: {% equation %}\frac{s}{r}{% endequation %} הוא <strong>קירוב טוב </strong>של {% equation %}x{% endequation %}, ולכן הולך להופיע בפיתוח לשברים משולבים של {% equation %}x{% endequation %}. כזכור, בפוסט על אלגוריתם הערכת פאזה ראינו בדיוק כיצד ניתן להגדיל את ההסתברות לקבלת קירוב טוב (עוד קיוביטים), אז מה שנצטרך לעשות הוא להבין כמה טוב צריך להיות <strong>הקירוב הטוב</strong> הזה.

עוד עניין שאין לנו דרך להתמודד איתו הוא ש-{% equation %}\frac{s}{r}{% endequation %} צריך להיות <strong>שבר מצומצם</strong>. אם למשל {% equation %}s=7{% endequation %} ו-{% equation %}r=63{% endequation %}, אז {% equation %}\frac{s}{r}=\frac{7}{63}=\frac{1}{9}{% endequation %}, ואז מה שהפיתוח לשברים משולבים ייתן לנו הוא את {% equation %}\frac{1}{9}{% endequation %}. זה כמובן אותו מספר בדיוק כמו {% equation %}\frac{7}{63}{% endequation %}, אבל אנחנו מעוניינים במספר 63 שנמצא במכנה, לא ב-9. אז כדי שהאלגוריתם יצליח, ה-{% equation %}0\le s<r{% endequation %} שנבחר באקראי צריך להיות זר ל-{% equation %}r{% endequation %}. למרבה המזל, רוב ה-{% equation %}s{% endequation %}-ים הללו אכן כאלו, אז זו לא בעיה אמיתית - אבל מי שרוצים להיות ממש זהירים יכולים, בהינתן המספר שהתקבל במכנה, לנסות גם כפולות שלו - אם היינו מנסים לקחת את ה-9 שקיבלנו במכנה, לכפול אותו ב-7 ולנסות לפרק לגורמים את {% equation %}N{% endequation %} עם ה-{% equation %}63{% endequation %} שקיבלנו, היינו מצליחים; הנסיונות הללו לא מפריעים לשום דבר ומגדילים עוד קצת את הסיכוי שנצליח, אבל כנראה שאפשר גם בלעדיהם.

אוקיי, בואו נעבור לשברים משולבים! ספציפית אל המספר {% equation %}\frac{314159}{100000}{% endequation %} שהבטחתי למצוא לו סדרת קירובים טובה יותר מאשר {% equation %}3,3.1,3.14{% endequation %} וכן הלאה. הטכניקה שבה אשתמש תיראה מוזרה במבט ראשון, אבל סמכו עלי - היא עובדת. כזכור, אי שם בבית הספר לימדו אותנו שיש משהו שנקרא "שבר מדומה" שהוא שבר שבו המונה גדול מהמכנה. שבר כזה אפשר להפריד לסכום שנקרא "מספר מעורב" של החלק השלם ועוד החלק השברי שהוא בין 0 ל-1. במקרה שלנו:

{% equation %}\frac{314159}{100000}=3+\frac{14159}{100000}{% endequation %}

עכשיו אני עושה את הטריק המרכזי שלי: אני משתמש בכך שבאופן כללי, {% equation %}\frac{a}{b}=\frac{1}{\frac{b}{a}}{% endequation %} כדי לכתוב

{% equation %}\frac{14159}{100000}=\frac{1}{\frac{100000}{14159}}{% endequation %}

מה הולך פה? קודם היה לנו שבר "אמיתי", שבו המונה <strong>קטן</strong> מהמכנה; עכשיו המונה והמכנה התהפכו, אז שוב קיבלנו שבר מדומה שאנחנו יכולים להפריד למספר שלם ועוד שבר. בשביל לעשות את זה, צריך לחלק את 100,000 ב-14,159; המנה שנקבל היא החלק השלם, והשארית שנקבל היא מה שנשאר על השבר: {% equation %}\frac{100000}{14159}=7+\frac{887}{14159}{% endequation %}.

אם שותלים את הביטוי הזה בחישוב שכבר עשינו, מקבלים

{% equation %}3+\frac{14159}{100000}=3+\frac{1}{7+\frac{887}{14159}}{% endequation %}

אפשר להמשיך עם זה ולהתעלל גם ב--{% equation %}\frac{887}{14159}{% endequation %}, אבל אפשר גם לקחת הפסקה לרגע ולהגיד "אוקיי, בואו נתעלם לגמרי מה-{% equation %}\frac{887}{14159}{% endequation %}, מה קיבלנו עכשיו?" ואז יש לנו את השבר

{% equation %}3+\frac{1}{7}=\frac{22}{7}{% endequation %}

הופה! הנה צץ לנו הקירוב המצוין לפאי שדיברתי עליו קודם! כאילו במטה קסם. ובכן, כן, זה <strong>באמת</strong> קסם, עד כמה שדברים שקורים במתמטיקה הם קסם; זה הקסם שמאפשר לנו לסיים את האלגוריתם של שור. <strong>למה</strong> זה קורה? סבלנות! עוד אוכיח את זה באופן מלא בפוסט הזה.

נחזור אל ה-{% equation %}\frac{887}{14159}{% endequation %}. בשלב הזה אנחנו כבר יודעים מה לעשות - לחלק את 14159 ב-887 ולראות מה המנה ומה השארית, ואז לכתוב

{% equation %}\frac{887}{14159}=\frac{1}{15+\frac{854}{887}}{% endequation %}

אם נשתול את זה בביטוי המקורי נקבל משהו שהוא כבר בלתי קריא בעליל:

{% equation %}3+\frac{1}{7+\frac{1}{15+\frac{854}{887}}}{% endequation %}

בגלל שזה בלתי קריא, משתמשים לפעמים בשיטת סימון אחרת, שבה לא צריך לרדת למטה עוד ועוד:

{% equation %}3+\frac{1}{7+}\frac{1}{15+}\frac{1}{887/854}{% endequation %}

אבל אני אשתמש בשיטת סימון עוד יותר קומפקטית: הרי לא באמת צריך את כל הפלוסים וה-1 חלקי הללו, אנחנו מתעניינים רק במספרים שליד הפלוסים. אז אפשר לכתוב

{% equation %}\left[3,7,15,\frac{887}{854}\right]{% endequation %}

זו צורת הכתיב הנפוצה והמקובלת. הנה הגדרה פורמלית של מה היא אומרת:

{% equation %}\left[a_{0},a_{1},\ldots a_{n}\right]=a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\frac{1}{\cdots+\frac{1}{a_{n}}}}}{% endequation %}

ועכשיו אפשר להמשיך יותר בנוחות. נחלק את 887 ב-854 ונקבל מנה 1 ושארית 33, כלומר השלב הבא הוא

{% equation %}\left[3,7,15,1,\frac{854}{33}\right]{% endequation %}

בשלב הבא נחלק 854 ב-33 ונקבל מנה 25 ושארית 29, ובואו נמשיך גם לשלב הבא כי הבנו את הקטע:

{% equation %}\left[3,7,15,1,25,\frac{33}{29}\right]=\left[3,7,15,1,25,1,\frac{29}{4}\right]={% endequation %}

{% equation %}=\left[3,7,15,1,25,1,7,\frac{4}{1}\right]{% endequation %}

וזה השלב האחרון, כי 4 מתחלק ב-1 ללא שארית! זו הצורה ה"סופית" של השבר המשולב:

{% equation %}\left[3,7,15,1,25,1,7,4\right]{% endequation %}

כלומר, אנחנו מרגישים רגועים לומר שסיימנו כשהאיבר האחרון, הימני ביותר, הוא עצמו מספר שלם ולא שבר.

ואיך כל זה עוזר לנו בכלל? כפי שראינו קודם, כבר כש"עצרנו" את החישוב אחרי שקיבלנו את ה-7 הראשון והתעלמנו מהשארית, קיבלנו את הקירוב {% equation %}\frac{22}{7}{% endequation %} המצוין. באותו אופן אפשר לעצור את הקירוב גם בשלבים מתקדמים יותר ולקבל קירובים מצויינים אחרים. למשל:

{% equation %}\left[3,7,15\right]=3+\frac{1}{7+\frac{1}{15}}=3+\frac{1}{\frac{106}{15}}=\frac{333}{106}{% endequation %}

גם זה קירוב מפורסם של פאי, וכן הלאה - הבנו את הרעיון. שימו לב, אגב, שלא עבדנו עם {% equation %}\pi{% endequation %} בכלל; התחלנו עם המספר {% equation %}3.14159{% endequation %} ומצאנו סדרת קירובים <strong>אליו</strong>; בגלל שהוא קירוב לא רע של פאי, קיבלנו שסדרת הקירובים החלקיים עד כה נותנת גם את הקירובים המצויינים של {% equation %}\pi{% endequation %}. אם היינו מלכתחילה רוצים לחשב שבר משולב עבור {% equation %}\pi{% endequation %} היינו נתקלים בשתי בעיות - החישוב קצת יותר מסובך, והשבר המשולב המתקבל צריך להיות <strong>אינסופי</strong>; כדי להתחמק מהסיבוך הזה שלא דרוש לי הסתפקתי בלתאר איך מחשבים שבר משולב עבור מספר שהוא מלכתחילה שבר - ומה שראינו הוא שהשבר המשולב שאנחנו בונים אכן נותן סדרה מצויינת של קירובים לאותו השבר. זה המקרה הרלוונטי לנו כי כזכור, אנחנו מקבלים מאלגוריתם הערכת הפאזה מספר <strong>רציונלי </strong>{% equation %}x{% endequation %} שבתקווה {% equation %}\frac{s}{r}{% endequation %} הוא קירוב מצויין אליו. אם {% equation %}x{% endequation %} הוא מספר רציונלי, אנחנו יודעים איך לחשב לו שבר משולב ואז לקבל ממנו את סדרת הקירובים האופטימלית שהוא נותן - זה חישוב מאוד פשוט שכולל בסך הכל פעולות של חילוק עם שארית וחישובים אריתמטיים פשוטים יותר. קל לתכנת את זה והריצה של החלק הזה לוקחת שברירי שניה.

<h2>בונוס: איך מוכיחים את כל הקטע הזה של השברים המשולבים?</h2>

יופי, סיימנו עם האלגוריתם של שור ואפשר לעבור לתורת המספרים נטו! בואו נעבור לתיאור פורמלי של עניין ה<strong>קירוב טוב</strong> הזה. נתחיל עם סימון: אם {% equation %}x{% endequation %} הוא מספר רציונלי עם פיתוח לשבר משולב {% equation %}\left[a_{0},a_{1},\ldots,a_{n}\right]{% endequation %}, אני אסמן את סדרת הקירובים שמתקבלת מהפיתוח הזה בתור {% equation %}\frac{p_{0}}{q_{0}},\frac{p_{1}}{q_{1}},\frac{p_{2}}{q_{2}},\ldots,\frac{p_{n}}{q_{n}}{% endequation %}. כלומר, {% equation %}\frac{p_{k}}{q_{k}}=\left[a_{0},a_{1},\ldots,a_{k}\right]{% endequation %}. 

הנה דברים שאפשר להראות אבל לא אראה הפעם: {% equation %}q_{0}<q_{1}<q_{2}<\ldots<q_{n}{% endequation %}, כלומר המכנה הולך וגדל ככל שמתקדמים בסדרה; {% equation %}p_{k},q_{k}{% endequation %} זרים זה לזה לכל אינדקס {% equation %}k{% endequation %}; והקירוב {% equation %}\frac{p_{k}}{q_{k}}{% endequation %} הוא טוב במובן הבא:

{% equation %}\left|x-\frac{p_{k}}{q_{k}}\right|<\frac{1}{q_{k}q_{k+1}}<\frac{1}{q_{k}^{2}}{% endequation %}

כשהמעבר השני נובע מכך ש-{% equation %}q_{k}<q_{k+1}{% endequation %} (עבור {% equation %}k=n{% endequation %} הנוסחה לא עובדת כי אין {% equation %}q_{k+1}{% endequation %} אבל ממילא בשלב הזה ההפרש הוא 0).

{% equation %}\frac{p_{k}}{q_{k}}{% endequation %} הוא <strong>הקירוב הטוב ביותר</strong> במובן זה שלכל {% equation %}1\le d\le q_{k}{% endequation %} ולכל {% equation %}c{% endequation %} מתקיים

{% equation %}\left|x-\frac{p_{k}}{q_{k}}\right|\le\left|x-\frac{c}{d}\right|{% endequation %}

כלומר, אם מסתכלים על כל המספרים הרציונליים עם מכנה שהוא לכל היותר {% equation %}q_{k}{% endequation %}, לא נמצא אף אחד שהוא קירוב יותר טוב ל-{% equation %}x{% endequation %} מאשר {% equation %}\frac{p_{k}}{q_{k}}{% endequation %}.

יפה, כל אלו הם משפטים מעניינים, אבל המשפט שמעניין אותי באמת הוא זה שמבטיח לנו שקירוב טוב בהכרח יופיע בפיתוח לשבר משולב, וסוף סוף אפשר לנסח אותו פורמלית: אם {% equation %}c,d{% endequation %} זרים זה לזה, עם {% equation %}1\le d{% endequation %}, ומתקיים

{% equation %}\left|x-\frac{c}{d}\right|<\frac{1}{2d^{2}}{% endequation %}

אז <strong>בודאות</strong> קיים {% equation %}k{% endequation %} כך ש-{% equation %}\frac{c}{d}=\frac{a_{k}}{b_{k}}{% endequation %} עבור איבר {% equation %}\frac{a_{k}}{b_{k}}{% endequation %} בסדרת הקירובים שמתקבלת מהפיתוח של {% equation %}x{% endequation %} לשבר משולב.

איך מוכיחים את זה?

טוב, אני אצטרך שנכיר עוד כמה דברים על שברים משולבים כדי להתקדם. הדבר הראשון הוא נוסחה די משוגעת שעבור שבר משולב {% equation %}\left[a_{0},a_{1},\ldots,a_{n},a_{n+1}\right]{% endequation %} נותנת לנו את {% equation %}\frac{p_{n+1}}{q_{n+1}}{% endequation %} - האיבר הבא בסדרת הקירובים - אם נתונים לנו {% equation %}\frac{p_{n}}{q_{n}},\frac{p_{n-1}}{q_{n-1}}{% endequation %} ו-{% equation %}a_{n+1}{% endequation %}. הנה הנוסחה:

{% equation %}\frac{p_{n+1}}{q_{n+1}}=\frac{a_{n+1}p_{n}+p_{n-1}}{a_{n+1}q_{n}+q_{n-1}}{% endequation %}

בואו נראה את זה בפעולה עבור {% equation %}\left[3,7,15,1,25,1,7,4\right]{% endequation %}, השבר המשולב שכבר מצאנו עבור הקירוב לפאי. כזכור, שני הקירובים הראשונים שקיבלנו היו {% equation %}\frac{3}{1}{% endequation %} ו-{% equation %}\frac{22}{7}{% endequation %}, והקירוב השלישי היה {% equation %}\frac{333}{106}{% endequation %}. לכאורה כדי לקבל את הקירוב השלישי אנחנו לא יכולים להיעזר בשני הראשונים; אנחנו חייבים לבצע את כל החישוב {% equation %}3+\frac{1}{7+\frac{1}{15}}{% endequation %}; אי אפשר לקחת את {% equation %}\frac{22}{7}=3+\frac{1}{7}{% endequation %} ופשוט "לשתול" את {% equation %}15{% endequation %} בתוכו בצורה פשוטה. אבל בואו נראה מה קורה עם הנוסחה:

{% equation %}\frac{a_{2}p_{1}+p_{0}}{a_{2}q_{1}+q_{0}}=\frac{15\cdot22+3}{15\cdot7+1}=\frac{333}{106}{% endequation %}

קסם! תקשיבו לי, זה פשוט קסם! אין לי שמץ של מושג איך זה קורה למרות שלדעתי כבר ראיתי כמה פעמים את ההוכחה. בואו נראה אותה שוב ביחד.

כפי שניתן לנחש, מוכיחים את הטענה באינדוקציה. המקרה הפשוט ביותר שהוא היא רלוונטית הוא {% equation %}n=1{% endequation %}. במקרה הזה, השבר המשולב שלנו הוא {% equation %}\left[a_{0},a_{1},a_{2}\right]{% endequation %} והפיתוחים החלקיים שלו הם

{% equation %}\frac{p_{0}}{q_{0}}=\frac{a_{0}}{1}{% endequation %}

{% equation %}\frac{p_{1}}{q_{1}}=a_{0}+\frac{1}{a_{1}}=\frac{a_{0}a_{1}+1}{a_{1}}{% endequation %}

מאלו אנחנו יכולים להסיק:

{% equation %}p_{0}=a_{0},q_{0}=1{% endequation %}

{% equation %}p_{1}=a_{0}a_{1}+1,q_{1}=a_{1}{% endequation %}

עבור האיבר הבא החישוב קצת יותר מסובך אבל נעשה אותו במפורש:

{% equation %}\frac{p_{2}}{q_{2}}=a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}}}=a_{0}+\frac{a_{2}}{a_{2}a_{1}+1}=\frac{a_{2}a_{0}a_{1}+a_{0}+a_{2}}{a_{2}a_{1}+1}={% endequation %}

{% equation %}=\frac{a_{2}\left(a_{0}a_{1}+1\right)+a_{0}}{a_{2}a_{1}+1}=\frac{a_{2}p_{1}+p_{0}}{a_{2}q_{1}+q_{0}}{% endequation %}

קיבלנו את הנוסחה במקרה הזה, ועכשיו רק נשאר לסיים באינדוקציה את המקרה הכללי. כאן פשוט <strong>חייב</strong> לבוא איזה טיעון מתוחכם, כי הנוסחה הזו מפשטת לנו מאוד משהו שנראה מבעית בהתחלה. הנה ההתחכמות: במקרה הכללי, השבר המשולב שמתקבל מהאיברים הראשונים עד {% equation %}a_{n}{% endequation %} הוא

{% equation %}\left[a_{0},a_{1},\ldots,a_{n}\right]{% endequation %}

ועבורו יש לנו את נוסחת הנסיגה

{% equation %}\left[a_{0},a_{1},\ldots,a_{n}\right]=\frac{a_{n}p_{n-1}+p_{n-2}}{a_{n}q_{n-1}+q_{n-2}}{% endequation %}

עכשיו הטיעון המתוחכם: {% equation %}p_{n-1},q_{n-1},p_{n-2},q_{n-2}{% endequation %} מתקבלים מ-{% equation %}\left[a_{0},a_{1},\ldots,a_{n-1}\right]{% endequation %} ומ-{% equation %}\left[a_{0},a_{1},\ldots,a_{n-2}\right]{% endequation %}; השברים המשולבים הללו לא תלויים באיבר האחרון, ולכן המספרים הללו יישארו זהים גם אם נשתול בתור האיבר האחרון משהו אחר, למשל את {% equation %}a_{n}+\frac{1}{a_{n+1}}{% endequation %}. אבל מה זה {% equation %}\left[a_{0},a_{1},\ldots,a_{n-1},a_{n}+\frac{1}{a_{n+1}}\right]{% endequation %}? אם נפתח את ההגדרה, נראה שזה

{% equation %}a_{0}+\frac{1}{a_{1}+\frac{1}{a_{2}+\frac{1}{\cdots+\frac{1}{a_{n}+\frac{1}{a_{n+1}}}}}}{% endequation %}

כלומר, זה פשוט המספר {% equation %}\left[a_{0},a_{1},\ldots,a_{n-1},a_{n},a_{n+1}\right]=\frac{p_{n+1}}{q_{n+1}}{% endequation %}, רק שעבור הצורה הקודמת אפשר להשתמש בנוסחת הנסיגה:

{% equation %}\left[a_{0},a_{1},\ldots,a_{n-1},a_{n}+\frac{1}{a_{n+1}}\right]=\frac{\left(a_{n}+\frac{1}{a_{n+1}}\right)p_{n-1}+p_{n-2}}{\left(a_{n}+\frac{1}{a_{n+1}}\right)q_{n-1}+q_{n-2}}{% endequation %}

זה קצת מזוויע אבל נכפול מונה ומכנה ב-{% equation %}a_{n+1}{% endequation %} ונקבל

{% equation %}\frac{\left(a_{n+1}a_{n}+1\right)p_{n-1}+a_{n+1}p_{n-2}}{\left(a_{n+1}a_{n}+1\right)q_{n-1}+a_{n+1}q_{n-2}}=\frac{a_{n+1}\left(a_{n}p_{n-1}+p_{n-2}\right)+p_{n-1}}{a_{n+1}\left(a_{n}q_{n-1}+q_{n-2}\right)+q_{n-1}}=\frac{a_{n+1}p_{n}+p_{n-1}}{a_{n+1}q_{n}+q_{n-1}}{% endequation %}

וזה בדיוק הביטוי שקיווינו לקבל! זה מסיים את ההוכחה הזו.

בעזרת הנוסחה הזו אפשר לקבל נוסחה מקסימה נוספת, שמקשרת בין {% equation %}\frac{p_{n}}{q_{n}}{% endequation %} ובין האיבר הקודם לו, {% equation %}\frac{p_{n-1}}{q_{n-1}}{% endequation %}:

{% equation %}q_{n}p_{n-1}-p_{n}q_{n-1}=\left(-1\right)^{n}{% endequation %}

ההוכחה של זה היא באינדוקציה פשוטה למדי: במקרה הבסיס {% equation %}n=1{% endequation %} אנו מתבססים על כך שבפיתוח של {% equation %}\left[a_{0},a_{1},\ldots,a_{k}\right]{% endequation %} מקבלים, כמו שכבר ראינו, {% equation %}\frac{p_{0}}{q_{0}}=\frac{a_{0}}{1}{% endequation %} ולכן {% equation %}p_{0}=a_{0},q_{0}=1{% endequation %} וש-{% equation %}\frac{p_{1}}{q_{1}}=a_{0}+\frac{1}{a_{1}}=\frac{a_{0}a_{1}+1}{a_{1}}{% endequation %}, כלומר {% equation %}p_{1}=a_{0}a_{1}+1{% endequation %} ו-{% equation %}q_{1}=a_{1}{% endequation %}. אנו מציבים את זה בנוסחה ומקבלים

{% equation %}q_{1}p_{0}-p_{1}q_{0}=a_{1}a_{0}-\left(a_{0}a_{1}+1\right)=1{% endequation %}

זה מסיים את המקרה הזה. ובאופן כללי? אם נניח שהקשר מתקיים עבור {% equation %}n,n-1{% endequation %}, בואו נוכיח אותו עבור {% equation %}n+1,n{% endequation %} תוך ניצול נוסחת הנסיגה שכבר מצאנו, שהיא כזכור

{% equation %}p_{n+1}=a_{n+1}p_{n}+p_{n-1}{% endequation %}

{% equation %}q_{n+1}=a_{n+1}q_{n}+q_{n-1}{% endequation %}

נציב את אלו בנוסחה שאנחנו רוצים להוכיח עבורה את הטענה:

{% equation %}q_{n+1}p_{n}-p_{n+1}q_{n}=\left(a_{n+1}q_{n}+q_{n-1}\right)p_{n}-\left(a_{n+1}p_{n}+p_{n-1}\right)q_{n}={% endequation %}

{% equation %}=\left(a_{n+1}q_{n}p_{n}-a_{n+1}p_{n}q_{n}\right)+\left(q_{n-1}p_{n}-p_{n-1}q_{n}\right)={% endequation %}

{% equation %}=-\left(p_{n-1}q_{n}-q_{n-1}p_{n}\right)=-\left(-1\right)^{n}=\left(-1\right)^{n+1}{% endequation %}

מה שמסיים גם את זה! עכשיו סוף סוף יש לנו את הכלים שאנחנו צריכים כדי להוכיח את הטענה המקורית שלנו: שעבור {% equation %}x{% endequation %} רציונלי, אם ניקח {% equation %}\frac{c}{d}{% endequation %} חיובי שמקיים

{% equation %}\left|x-\frac{c}{d}\right|<\frac{1}{2d^{2}}{% endequation %}

אז {% equation %}\frac{c}{d}{% endequation %} יופיע בפיתוח לשבר משולב של {% equation %}x{% endequation %}. נקודה אחת שצריך לשים לב אליה ולא אוכיח פורמלית היא שהפיתוח לשבר משולב שבו כל האיברים הם שלמים הוא <strong>יחיד</strong> למעט אפשרות להתחכם קצת בשלב האחרון: אפשר להחליף את {% equation %}\left[a_{0},a_{1},\ldots,a_{n}\right]{% endequation %} ב-{% equation %}\left[a_{0},a_{1},\ldots,a_{n}-1,1\right]{% endequation %}, כי {% equation %}a_{n}-1+\frac{1}{1}=a_{n}{% endequation %}. אם כן, אם אני אראה שיש ל-{% equation %}x{% endequation %} פיתוח <strong>כלשהו </strong>לשבר משולב שבו {% equation %}\frac{c}{d}{% endequation %} מופיע לפני הסוף, סיימנו. מצד שני, בזכות ההתחכמות שהראיתי, אפשר תמיד להניח שכשאנחנו לוקחים פיתוח של משהו לשבר משולב, אנחנו יכולים לשלוט על האם הפיתוח הוא מאורך <strong>זוגי</strong> או <strong>אי זוגי</strong>, כלומר האם {% equation %}q_{n}p_{n-1}-p_{n}q_{n-1}{% endequation %} הוא 1 או דווקא {% equation %}-1{% endequation %}; אני הולך להשתמש בזה בקרוב.

עכשיו אפשר לגשת סוף סוף לעניינים. מכיוון ש-{% equation %}\frac{c}{d}{% endequation %} הוא עצמו מספר רציונלי, קיים לו פיתוח לשבר משולב שהאיבר האחרון שלו יסומן ב-{% equation %}\frac{p_{n}}{q_{n}}{% endequation %}:

{% equation %}\frac{c}{d}=\frac{p_{n}}{q_{n}}=\left[a_{0},a_{1},\ldots,a_{n}\right]{% endequation %}

כאשר כאמור בהמשך אני אגיד אם {% equation %}n{% endequation %} זוגי או לא, בהתאם למה שיתאים לי. הרעיון עכשיו הוא למצוא {% equation %}\lambda{% endequation %} רציונלי כלשהו כך שמתקיים

{% equation %}x=\left[a_{0},a_{1},\ldots,a_{n},\lambda\right]{% endequation %}

שימו לב: זה לא הפיתוח המלא של {% equation %}x{% endequation %} לשברים משולבים! אבל אם {% equation %}\lambda\ge1{% endequation %} אפשר להמשיך את הפיתוח - לפתח גם את {% equation %}\lambda{% endequation %} לשבר משולב ולהוסיף את זה להמשך הפיתוח. זה נשמע מבלבל, אבל זה בדיוק מה שעשינו בדוגמה של פאי שכל כך התעקשתי עליה משום מה. הגעתי לביטוי כמו

{% equation %}\left[3,7,15,1,\frac{854}{33}\right]{% endequation %}

ואז פשוט המשכתי עם {% equation %}\frac{854}{33}{% endequation %}, בעזרת אותה טכניקה שבה מצאתי את האיברים הקודמים בסדרה. אם כן, ה-{% equation %}\lambda{% endequation %} הוא ה-{% equation %}\frac{854}{33}{% endequation %} שלנו כאן - אבל קודם צריך להשתכנע בכך שהוא קיים ושהוא גדול או שווה ל-1.

החלק היפה הוא שאם {% equation %}\lambda{% endequation %} קיים, אנחנו יודעים בדיוק איזו נוסחה שמערבת את {% equation %}x{% endequation %} הוא אמור לקיים, כי זה מה שטרחתי להוכיח קודם:

{% equation %}x=\left[a_{0},a_{1},\ldots,a_{n},\lambda\right]=\frac{\lambda p_{n}+p_{n-1}}{\lambda q_{n}+q_{n-1}}{% endequation %}

אנחנו רוצים לחלץ את {% equation %}\lambda{% endequation %} מפה, אז נכפול את שני האגפים ב-{% equation %}\lambda q_{n}+q_{n-1}{% endequation %} ונקבל

{% equation %}\lambda q_{n}x+q_{n-1}x=\lambda p_{n}+p_{n-1}{% endequation %}

נעביר אגפים ונוציא את {% equation %}\lambda{% endequation %} החוצה:

{% equation %}\lambda\left(q_{n}x-p_{n}\right)=p_{n-1}-q_{n-1}x{% endequation %}

ולסיום נחלק ב-{% equation %}q_{n}x-p_{n}{% endequation %} ונקבל

{% equation %}\lambda=\frac{p_{n-1}-q_{n-1}x}{q_{n}x-p_{n}}{% endequation %}

הביטוי הזה מוגדר תמיד, למעט במקרה שבו {% equation %}x=\frac{p_{n}}{q_{n}}{% endequation %} ואז נקבל במכנה 0; אבל המקרה הזה הוא טריוויאלי, כי {% equation %}\frac{p_{n}}{q_{n}}{% endequation %} הוא כזכור מה שרצינו לטעון שמופיע בפיתוח של {% equation %}x{% endequation %}, ולכן אם הוא עצמו {% equation %}x{% endequation %} בוודאי שהוא מופיע!

אז נניח ש-{% equation %}x\ne\frac{p_{n}}{q_{n}}{% endequation %}. אנחנו יודעים (זו הייתה ההנחה שלנו) ש-{% equation %}\left|x-\frac{p_{n}}{q_{n}}\right|<\frac{1}{2q_{n}^{2}}{% endequation %} ולכן אפשר לסמן את זה

{% equation %}x-\frac{p_{n}}{q_{n}}=\frac{\delta}{2q_{n}^{2}}{% endequation %}

כאשר {% equation %}0<\left|\delta\right|<1{% endequation %}. נעביר אגף ונקבל

{% equation %}x=\frac{p_{n}}{q_{n}}+\frac{\delta}{2q_{n}^{2}}{% endequation %}

עכשיו אני רוצה לקחת את זה ולהציב בתוך {% equation %}\lambda=\frac{p_{n-1}-q_{n-1}x}{q_{n}x-p_{n}}{% endequation %}. מכיוון שנקבל ביטוי פשוט אבל עם שלב ביניים מסובך, בואו נטפל במונה ובמכנה בנפרד. קודם כל המכנה:

{% equation %}q_{n}x-p_{n}=q_{n}\left(\frac{p_{n}}{q_{n}}+\frac{\delta}{2q_{n}^{2}}\right)-p_{n}=p_{n}+\frac{\delta}{2q_{n}}-p_{n}=\frac{\delta}{2q_{n}}{% endequation %}

אוקיי, זה לא היה כל כך נורא! עכשיו המונה:

{% equation %}p_{n-1}-q_{n-1}x=p_{n-1}-\frac{p_{n}q_{n-1}}{q_{n}}-\frac{q_{n-1}\delta}{2q_{n}^{2}}{% endequation %}

זה נראה מזוויע, אבל זוכרים את הנוסחה {% equation %}q_{n}p_{n-1}-p_{n}q_{n-1}=1{% endequation %}? היא מתחבאת כאן, רק צריך להעלות את ה-{% equation %}p_{n-1}{% endequation %} הזה למעלה:

{% equation %}p_{n-1}-\frac{p_{n}q_{n-1}}{q_{n}}-\frac{q_{n-1}\delta}{2q_{n}^{2}}=\frac{p_{n-1}q_{n}-p_{n}q_{n-1}}{q_{n}}-\frac{q_{n-1}\delta}{2q_{n}^{2}}=\frac{\left(-1\right)^{n}}{q_{n}}-\frac{q_{n-1}\delta}{2q_{n}^{2}}{% endequation %}

עכשיו, לחלק את זה ב-{% equation %}\frac{\delta}{2q_{n}}{% endequation %} זה כמו לכפול את זה ב-{% equation %}\frac{2q_{n}}{\delta}{% endequation %} (מותר לנו כי {% equation %}\delta\ne0{% endequation %} כי {% equation %}x\ne\frac{p_{n}}{q_{n}}{% endequation %}). נקבל:

{% equation %}\lambda=\frac{2q_{n}}{\delta}\left(\frac{\left(-1\right)^{n}}{q_{n}}-\frac{q_{n-1}\delta}{2q_{n}^{2}}\right)=\left(-1\right)^{n}\frac{2}{\delta}-\frac{q_{n-1}}{q_{n}}{% endequation %}

וזה יצא... ממש פשוט! עכשיו, כזכור אנחנו רוצים לקבל {% equation %}\lambda>1{% endequation %}; בשביל זה אנחנו חייבים להבטיח שהביטוי {% equation %}\left(-1\right)^{n}\frac{2}{\delta}{% endequation %} ייצא חיובי ולא שלילי, זה מחזיר אותנו לבחירה של {% equation %}n{% endequation %} בהתחלה; אם {% equation %}\delta>0{% endequation %} אז בוחרים את {% equation %}n{% endequation %} להיות זוגי ומקבלים {% equation %}\left(-1\right)^{n}=1{% endequation %}, ואם {% equation %}\delta<0{% endequation %} בוחרים {% equation %}n{% endequation %} אי זוגי ומקבלים {% equation %}\left(-1\right)^{n}=-1{% endequation %}. בכל מקרה אנחנו לבסוף מקבלים

{% equation %}\lambda=\frac{2}{\left|\delta\right|}-\frac{q_{n-1}}{q_{n}}{% endequation %}

יותר מזה, בגלל שסדרת המכנים בפיתוח לשבר משולב היא עולה, {% equation %}q_{n-1}<q_{n}{% endequation %} ולכן {% equation %}\frac{q_{n-1}}{q_{n}}<1{% endequation %} ומצד שני בגלל ש-{% equation %}\left|\delta\right|<1{% endequation %} אז {% equation %}\frac{2}{\left|\delta\right|}>2{% endequation %}, ואנחנו מקבלים {% equation %}\lambda>1{% endequation %}, כפי שרצינו. אנחנו מפתחים אותו לשבר משולב, מקבלים {% equation %}\lambda=\left[b_{1},\ldots,b_{m}\right]{% endequation %} ולבסוף מקבלים {% equation %}x=\left[a_{1},\ldots,a_{n},b_{1},\ldots,b_{m}\right]{% endequation %} - פיתוח מלא של {% equation %}x{% endequation %} לשבר משולב שבמהלכו מופיע {% equation %}\frac{a}{b}=\frac{p_{n}}{q_{n}}{% endequation %}, כפי שרצינו. זה מסיים את ההוכחה!

<h2>דברי סיכום ופרידה</h2>

ובכן, מה היה לנו הפעם? איך זה היה שונה מהפוסט הקודם שלי על האלגוריתם של שור? האלגוריתם מחולק קונספטואלית לשלושה חלקים; החלק הראשון, של הרדוקציה מבעיית הפירוק לגורמים אל בעיית הפרת הסדר, הוא חלק שהרחבתי עליו מאוד בפוסט ההוא והפעם לא נגעתי בו כי אין לי משהו נוסף לומר, אבל בשני החלקים האחרים הרחבתי לא מעט. ראשית, הצגתי באופן מפורש את שור בתור מקרה פרטי של אלגוריתם הערכת פאזה, שזה משהו שבכלל לא ניסיתי לעשות בפוסט הקודם (בואו לא נדבר על השאלה המביכה עד כמה הבנתי את זה בעצמי). שנית, הפעם התעמקתי קצת יותר במשפט הספציפי שקשור לשברים משולבים שמבטיח לנו שעם קצת מזל, ה-{% equation %}\frac{s}{r}{% endequation %} שאנחנו מחפשים יצוץ מתוך תוצאת אלגוריתם הערכת הפאזה. זה דרש גלישה נוספת לתורת המספרים במקום לחישוב קוונטי, אבל הנושא של שברים משולבים הוא כל כך כיפי שלא יכלתי להתאפק.

לאן הולכים מכאן? בסדרת הפוסטים הקודמת שלי, שור היה המטרה הסופית; אבל בסדרה הנוכחית, אני מקווה שעכשיו משהוצאנו את זה מהדרך, אפשר להראות כל מני דברים לא קשורים בעליל אבל מגניבים לא פחות. 