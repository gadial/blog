---
id: 3461
title: "מכפלות חצי ישרות"
date: 2017-07-21 21:00:47
layout: post
categories: 
  - אלגברה מופשטת
tags: 
  - מכפלות חצי ישרות
  - תורת החבורות
---
<h2>מבוא</h2>
במסגרת העיסוק שלנו בחבורות ראינו עוד ועוד דרכים לתאר חבורות ולבנות חבורות חדשות מחבורות קיימות. עכשיו הגיע הזמן לסגור את החור האחרון שאני רוצה לסגור כרגע (למרות שכמובן, זה רחוק מלהיות סוף הסיפור באופן כללי) ולהראות בניה כללית וחזקה למדי - בניה של <strong>מכפלה חצי ישרה</strong>, שהיא סוג של הכללה של המכפלה הישרה שהראיתי בפוסט קודם. מכפלה ישרה של שתי חבורות {% equation %}A,B{% endequation %} הייתה חבורה {% equation %}A\times B=\left\{ \left(a,b\right)\ |\ a\in A,b\in B\right\} {% endequation %} עם פעולת כפל "לפי קואורדינטות": {% equation %}\left(a_{1},b_{1}\right)\left(a_{2},b_{2}\right)=\left(a_{1}a_{2},b_{1}b_{2}\right){% endequation %}. התוצאה תמיד הייתה חבורה אבלית מסדר {% equation %}\left|A\right|\cdot\left|B\right|{% endequation %}. את הבניה הזו, שהיא "חיצונית" (לוקחים שתי חבורות שאין בהכרח קשר ביניהן ובונים חבורה חדשה) אפשר היה לתאר גם באופן "פנימי": אם {% equation %}G{% endequation %} חבורה עם תת-חבורות {% equation %}A,B{% endequation %} אז אפשר תמיד להגדיר קבוצה {% equation %}A\cdot B=\left\{ ab\ |\ a\in A,b\in B\right\} {% endequation %}. ראינו <a href="http://www.gadial.net/2017/04/19/direct_product_and_abelian_groups/">בפוסט קודם</a> שהקבוצה הזו היא מגודל {% equation %}\frac{\left|A\right|\cdot\left|B\right|}{\left|A\cap B\right|}{% endequation %}, ושאם מתקיים {% equation %}A\cap B=\left\{ e\right\} {% endequation %} וכמו כן <strong>{% equation %}A,B{% endequation %} </strong>שתיהן נורמליות ב-{% equation %}G{% endequation %}, אז {% equation %}AB\cong A\times B{% endequation %}. כלומר, <strong>בתנאים מסויימים</strong> החבורה {% equation %}AB{% endequation %} שווה למכפלה הישרה של {% equation %}A,B{% endequation %}. ובתנאים אחרים?

אני לא אוהב לעשות טיזינג בפוסטים, אז הנה העיקר: על הקבוצה {% equation %}A\times B{% endequation %} של הזוגות {% equation %}\left(a,b\right){% endequation %} אני יכול גם להגדיר פעולות נוספות, מתוחכמות קצת יותר, באמצעות מושג ה<strong>פעולה</strong> של חבורה על קבוצה. בואו ניקח פעולה של {% equation %}A{% endequation %} על {% equation %}B{% endequation %} שיש לה את התכונה הנוספת שכל איבר של {% equation %}A{% endequation %} פועל על {% equation %}B{% endequation %} בתור <strong>אוטומורפיזם</strong>, כלומר לא סתם מערבב את אברי {% equation %}B{% endequation %} אלא משמר את מבנה החבורה של {% equation %}B{% endequation %}. אז אפשר להגדיר פעולת כפל כזו: {% equation %}\left(a_{1},b_{1}\right)\left(a_{2},b_{2}\right)=\left(a_{1}\left(b_{1}\cdot a_{2}\right),b_{1}b_{2}\right){% endequation %}. מה הולך פה? הקואורדינטה השניה מוכפלת בדיוק כמו במכפלה ישרה. בקואורדינטה הראשונה מתרחש תהליך דו-שלבי: ראשית <strong>מפעילים</strong> את {% equation %}b_{1}{% endequation %} על {% equation %}a_{2}{% endequation %}, ורק אחר כך כופלים את התוצאה הזו ב-{% equation %}a_{1}{% endequation %}. הפעולה הזו מגדירה חבורה, שמסומנת ב-{% equation %}A\rtimes B{% endequation %}, וקוראים לדבר הזה <strong>מכפלה חצי ישרה</strong> של {% equation %}A{% endequation %} ב-{% equation %}B{% endequation %}.

כמעט מייד ברורים שני דברים: ראשית, עבור הפעולה הטריוויאלית שבה כל איבר פועל כמו הזהות ({% equation %}b\cdot a=a{% endequation %} לכל {% equation %}b\in B{% endequation %} ולכל {% equation %}a\in A{% endequation %}) קיבלנו שוב את המושג של מכפלה ישרה; ושנית, יש משהו מאוד לא סימטרי בהגדרה הזו, וכתוצאה מכך החבורות שנקבל כך יכולות להיות <strong>לא אבליות</strong>. זה דבר טוב: זה אומר שמצאנו בניה שתאפשר לנו לייצג חבורות לא אבליות מתוך חבורות קיימות, <strong>אפילו אם החבורות הקיימות כן אבליות</strong>. זה מה שמאפשר למכפלה חצי ישרה לתאר הרבה יותר סיטואציות משיכלנו קודם. זה מתבטא במשפט הבא: אם {% equation %}A,B{% endequation %} הן תתי-חבורות של {% equation %}G{% endequation %} כך ש-{% equation %}A\cap B=\left\{ e\right\} {% endequation %}, ואם {% equation %}A{% endequation %} נורמלית ב-{% equation %}G{% endequation %} (אבל {% equation %}B{% endequation %} <strong>לא בהכרח</strong> נורמלית) אז {% equation %}AB\cong A\rtimes B{% endequation %} כאשר הפעולה של {% equation %}B{% endequation %} על {% equation %}A{% endequation %} שמגדירה את המכפלה החצי ישרה היא פעולת ההצמדה של אברי {% equation %}A{% endequation %} על ידי אברי {% equation %}B{% endequation %}.

עכשיו, משהסברתי מה אנחנו רוצים להשיג, בואו ניכנס לפרטים.
<h2>מכפלה חצי ישרה "פנימית"</h2>
בואו נתחיל עם דוגמה קונקרטיות כי בתחום הזה אסור לרחף יותר מדי באוויר. {% equation %}S_{3}{% endequation %}: חבורת התמורות על {% equation %}\left\{ 1,2,3\right\} {% endequation %}. הנה לנו שתי תתי-חבורות שלה: {% equation %}A=\left\{ e,\left(1\ 2\ 3\right),\left(1\ 3\ 2\right)\right\} {% endequation %} ו-{% equation %}B=\left\{ e,\left(1\ 2\right)\right\} {% endequation %}. קל לוודא ששתיהן תתי-חבורות, וקל לוודא ש-{% equation %}A{% endequation %} נורמלית אבל {% equation %}B{% endequation %} <strong>לא נורמלית</strong>. למה? כי נורמליות פירושה להיות סגורים להצמדה; וכשמדברים על תמורות (וזו אחת הסיבות למה טוב לעבוד עם תמורות) המשמעות של הצמדה היא פשוטה - החלפה של התמורה הנוכחית בתמורה אחרת עם אותו מבנה מעגלי. מעל שלושה איברים יש לנו בסך הכל שתי תמורות שהמבנה המעגלי שלהן הוא מעגל יחיד מאורך 3, ולכן {% equation %}A{% endequation %} סגורה להצמדה, אבל יש לנו <strong>שלוש</strong> תמורות שונות עם מבנה מעגלי של מעגל יחיד מאורך 2, ולכן {% equation %}B{% endequation %} לא סגורה להצמדה ואינה נורמלית. מצד שני, אפשר לבדוק באופן ישיר שמתקיים {% equation %}AB=BA{% endequation %}. על פי מה שראינו בפוסט על מכפלות ישרות, די בכך ש-{% equation %}A,B{% endequation %} תתי-חבורות עבורן {% equation %}AB=BA{% endequation %} כדי להבטיח שהמכפלה {% equation %}AB{% endequation %} תהיה חבורה בעצמה, ומכיוון ש-{% equation %}A\cap B=\left\{ e\right\} {% endequation %} יוצא שזו חבורה עם {% equation %}3\cdot2=6{% endequation %} איברים, כלומר קיבלנו ש-{% equation %}AB=S_{3}{% endequation %} עצמה. מצד שני, אנחנו יודעים ש-{% equation %}S_{3}{% endequation %} אינה אבלית, ולכן לא ייתכן ש-{% equation %}AB\cong A\times B{% endequation %} מכיוון שמכפלה ישרה של חבורות כלשהן היא אבלית. מכאן שנדחף לנו בפרצוף הצורך למצוא "סוג חדש של מכפלה".

נעבור רגע לדבר על המקרה הכללי - {% equation %}A,B{% endequation %} תתי-חבורות של {% equation %}G{% endequation %} כך ש-{% equation %}A{% endequation %} נורמלית ו-{% equation %}B{% endequation %} לאו דווקא. איבר כללי של {% equation %}AB{% endequation %} הוא מהצורה {% equation %}ab{% endequation %} כך ש-{% equation %}a\in A{% endequation %} ו-{% equation %}b\in B{% endequation %}. אם ניקח שני איברים שונים של {% equation %}AB{% endequation %}, שאסמן {% equation %}a_{1}b_{1}{% endequation %} ו-{% equation %}a_{2}b_{2}{% endequation %} ואכפול אותם (באמצעות הפעולה שקיימת כבר ב-{% equation %}G{% endequation %}) אני אקבל {% equation %}\left(a_{1}b_{1}\right)\cdot\left(a_{2}b_{2}\right){% endequation %}. האיבר הזה לא מוצג כרגע בצורה ה"נחמדה" שבה אני רוצה להציג איברים של {% equation %}AB{% endequation %}, כי אני רוצה לקבל הצגה שבה יש לי איבר מ-{% equation %}A{% endequation %} שמוכפל באיבר מ-{% equation %}B{% endequation %} ותו לא. מכיוון שאני יודע ש-{% equation %}AB=BA{% endequation %} אני יכול להחליף את {% equation %}b_{1}a_{2}{% endequation %} במשהו מהצורה {% equation %}a^{\prime}b^{\prime}{% endequation %} ואז לקבל את ההצגה ה"נחמדה" שרציתי, אבל קצת איבדתי משהו - איבדתי את האיברים {% equation %}b_{1},a_{2}{% endequation %} שהוחלפו באיברים כלליים שאני לא יודע עליהם כלום. אז בואו ננסה גישה שונה להציג את המכפלה הזו שלא תצריך אותי לאבד מידע.

התעלול שבו אני אנקוט יתבסס על כך ש-{% equation %}A{% endequation %} היא תת-חבורה נורמלית, כלומר סגורה להצמדה; באופן כללי יותר הוא פשוט לא יעבוד. זה טריק ידוע, לקחת ביטוי שמתאר איבר בחבורה ולדחוף פנימה מכפלה באיבר וההופכי שלו. זה כמובן לא טריק שמוגבל לחבורות - אני מניח שרובכם מכירים את התעלול שמאפשר לי לראות ש-{% equation %}\frac{1}{\sqrt{2}}{% endequation %}זה אותו דבר כמו {% equation %}\frac{\sqrt{2}}{2}{% endequation %} - פשוט כופלים ב-{% equation %}\frac{\sqrt{2}}{\sqrt{2}}{% endequation %}. אז נעשה כאן את אותו הדבר עם {% equation %}b_{1}{% endequation %}:

{% equation %}a_{1}b_{1}a_{2}b_{2}=a_{1}b_{1}a_{2}b_{1}^{-1}b_{1}b_{2}{% endequation %}

כעת קיבלתי איבר שהוא מהצורה:

{% equation %}\left(a_{1}\left(b_{1}a_{2}b_{1}^{-1}\right)\right)\left(b_{1}b_{2}\right){% endequation %}

מכיוון ש-{% equation %}A{% endequation %} תת-חבורה נורמלית, {% equation %}b_{1}a_{2}b_{1}^{-1}\in A{% endequation %} ולכן קיבלתי הצגה כמכפלה של איבר ב-{% equation %}A{% endequation %} באיבר ב-{% equation %}B{% endequation %}, ואפילו מעט מאוד השתנה פה: את האיברים של {% equation %}B{% endequation %} פשוט כפלתי זה בזה לפי הסדר שלהם, ואילו את האיברים של {% equation %}A{% endequation %} גם כפלתי זה בזה, אבל רק אחרי שהצמדתי את {% equation %}a_{2}{% endequation %} בעזרת {% equation %}b_{1}{% endequation %}.

נחזור לדוגמא שלנו: אני אסתכל על האיברים הבאים של {% equation %}AB{% endequation %}: ראשית על {% equation %}\left(1\ 2\ 3\right)\left(1\ 2\right){% endequation %} ושנית על {% equation %}\left(1\ 3\ 2\right){% endequation %} (שמוכפל מימין ב-{% equation %}e{% endequation %} ואני לא טורח לכתוב זאת). המכפלה של שניהם היא {% equation %}\left(1\ 2\ 3\right)\left(1\ 2\right)\left(1\ 3\ 2\right){% endequation %} ועל פי הכלל שמצאנו, אפשר להצמיד את {% equation %}\left(1\ 3\ 2\right){% endequation %} על ידי {% equation %}\left(1\ 2\right){% endequation %} (כלומר, להחליף את 2 ב-1 ולהפך) ולקבל את {% equation %}\left(1\ 2\ 3\right)^{2}\cdot\left(1\ 2\right){% endequation %} , כלומר את {% equation %}\left(1\ 3\ 2\right)\left(1\ 2\right){% endequation %}. אם תבדקו ישירות תראו שזה אכן שווה ל-{% equation %}\left(1\ 2\ 3\right)\left(1\ 2\right)\left(1\ 3\ 2\right){% endequation %}.
<h2>מכפלה חצי ישרה "חיצונית"</h2>
מה שתיארתי עד כה היה מה שנקרא "מכפלה חצי ישרה פנימית". הסיטואציה הייתה שאני מתחיל מחבורה קיימת {% equation %}G{% endequation %}, מסתכל על תת-חבורות שלה שכבר מוגדרת בין איברים שלהן פעולת הכפל של {% equation %}G{% endequation %}, ומייצר מהן תת-חבורה אחרת של {% equation %}G{% endequation %}. כלומר, אני בסך הכל נותן אבחנה על הקשר בין שלוש תת-חבורות קיימות של {% equation %}G{% endequation %}. מה שמעניין יותר הוא האופן שבו אני יכול לקחת שתי חבורות {% equation %}A,B{% endequation %} <strong>שאין ביניהן שום קשר</strong> ולבנות מתוכן חבורה חדשה, גדולה יותר. בחבורה הגדולה יותר הזו אני אוכל למצוא תת-חבורות שיהיו איזומורפיות ל-{% equation %}A,B{% endequation %} ואני אקבל שהחבורה הזו היא המכפלה החצי ישרה של אותן תתי-חבורות. בואו ננסח פורמלית את מה שאני הולך לעשות.

ובכן, יהיו {% equation %}A,B{% endequation %} חבורות כלשהן. בנוסף אליהן אני צריך גם פעולה של {% equation %}B{% endequation %} על {% equation %}A{% endequation %}, אבל כפי שנראה בהמשך, לא סתם פעולה כלשהי (כלומר, הומומורפיזם של {% equation %}B{% endequation %} לתוך חבורת <strong>הפרמוטציות</strong> של {% equation %}A{% endequation %}) אלא פעולה שמכבדת את הפעולה של {% equation %}A{% endequation %}, דהיינו הומומורפיזם של {% equation %}B{% endequation %} לתוך חבורת <strong>האוטומורפיזמים</strong> של {% equation %}A{% endequation %}. אוטומורפיזם של {% equation %}A{% endequation %} הוא פונקציה {% equation %}f:A\to A{% endequation %} שהיא חח"ע ועל (עד כאן זה תיאור של <strong>פרמוטציה</strong>) שבנוסף לכך מקיימת {% equation %}f\left(a_{1}a_{2}\right)=f\left(a_{1}\right)f\left(a_{2}\right){% endequation %}, כלומר היא הומומורפיזם. נסמן ב-{% equation %}\text{Aut}\left(A\right){% endequation %} את חבורת האוטומורפיזמים של {% equation %}A{% endequation %}; אז אנחנו רוצים פעולה של {% equation %}B{% endequation %} שמתוארת על ידי הומומורפיזם {% equation %}\varphi:B\to\text{Aut}\left(A\right){% endequation %}. כן, החלק הזה מתחיל להיות מבלבל, עם הומומורפיזמים שמחזירים אוטומורפיזמים.

עכשיו אני מגדיר את החבורה {% equation %}G=A\rtimes_{\varphi}B{% endequation %} כך: זו הקבוצה {% equation %}A\times B\triangleq\left\{ \left(a,b\right)\ |\ a\in A,b\in B\right\} {% endequation %} עם פעולת הכפל {% equation %}\left(a_{1},b_{1}\right)\left(a_{2},b_{2}\right)=\left(a_{1}b_{1}\cdot a_{2},b_{1}b_{2}\right){% endequation %}. כאן {% equation %}b_{1}\cdot a_{2}{% endequation %} זה סימון מקוצר לפעולה של {% equation %}B{% endequation %}, כלומר {% equation %}b_{1}\cdot a_{2}\triangleq\varphi\left(b_{1}\right)\left(a_{2}\right){% endequation %}. צריך עכשיו להשתכנע בכך ש-{% equation %}G{% endequation %} היא חבורה, בכך ש-{% equation %}A,B{% endequation %} איזומורפיות לתתי-חבורות שלה, וש-{% equation %}G{% endequation %} היא מכפלה חצי ישרה פנימית של שתי-החבורות הללו. חוץ מזה אפשר יהיה גם להראות שתת החבורה שאיזומורפית ל-{% equation %}A{% endequation %} היא תת-חבורה נורמלית.

להוכיח ש-{% equation %}A\rtimes_{\varphi}B{% endequation %} זה... זה כואב. אין מנוס מלהודות בכך. צריך לעשות את כל החישובים ואין דרכי קיצור. בואו נלך אל הדבר שהוא תמיד הגרוע ביותר - אסוציאטיביות. מן הסתם האסוציאטיביות של {% equation %}A\rtimes_{\varphi}B{% endequation %} תנבע מהאסוציאטיביות של {% equation %}A,B{% endequation %} ומאיזו תכונה נחמדה של פעולת חבורה על קבוצה. בואו נעשה את הכל כולל הכל. אתם מוזמנים לדלג אם בא לכם.

{% equation %}\left[\left(a_{1},b_{1}\right)\left(a_{2},b_{2}\right)\right]\left(a_{3},b_{3}\right)=\left(a_{1}b_{1}\cdot a_{2},b_{1}b_{2}\right)\left(a_{3},b_{3}\right){% endequation %}

{% equation %}=\left(a_{1}\left(b_{1}\cdot a_{2}\right)\left(b_{1}b_{2}\cdot a_{3}\right),b_{1}b_{2}b_{3}\right){% endequation %}

עכשיו פסק זמן. בואו ניזכר בתכונה הבסיסית של פעולת חבורה: פעולה של מכפלת איברים אפשר לפרק לפעולה-על-פעולה. כלומר {% equation %}b_{1}b_{2}\cdot a_{3}=b_{1}\cdot\left(b_{2}\cdot a_{3}\right){% endequation %}.

כמו כן, במקרה הספציפי שלנו הפעולה, כזכור, היא <strong>אוטומורפיזם</strong> של {% equation %}A{% endequation %}. במילים אחרות, {% equation %}b\cdot\left(xy\right)=\left(b\cdot x\right)\left(b\cdot y\right){% endequation %} עבור {% equation %}x,y\in A{% endequation %}. שני הדברים הללו מאפשרים לי לבצע את השלב הבא, שיתבסס על כך ש:

{% equation %}\left(b_{1}\cdot a_{2}\right)\left(b_{1}b_{2}\cdot a_{3}\right)=\left(b_{1}\cdot a_{2}\right)\left(b_{1}\cdot\left(b_{2}\cdot a_{3}\right)\right)=b_{1}\cdot\left(a_{2}\left(b_{2}\cdot a_{3}\right)\right){% endequation %}

ולכן נקבל

{% equation %}\left(a_{1}\left(b_{1}\cdot a_{2}\right)\left(b_{1}b_{2}\cdot a_{3}\right),b_{1}b_{2}b_{3}\right)=\left(a_{1}\left[b_{1}\cdot\left(a_{2}\left(b_{2}\cdot a_{3}\right)\right)\right],b_{1}b_{2}b_{3}\right){% endequation %}

{% equation %}=\left(a_{1},b_{1}\right)\left(\left(a_{2}\left(b_{2}\cdot a_{3}\right)\right),b_{2}b_{3}\right){% endequation %}

{% equation %}=\left(a_{1},b_{1}\right)\left[\left(a_{2},b_{2}\right)\left(a_{3},b_{3}\right)\right]{% endequation %}

טוב, זה היה פחות כואב משחששתי, וכבונוס אפשר לראות יפה מאוד איפה נכנסת לתמונה העובדה שהפעולה של {% equation %}B{% endequation %} היא אוטומורפיזם. כשאני מעודד מההצלחה היחסית הזו בואו נעבור לבדוק את שאר תכונות החבורה.

מי יהיה איבר היחידה, זה די ברור: {% equation %}\left(e_{A},e_{B}\right){% endequation %}. זה נובע מייד מכך ש-{% equation %}e_{B}\cdot x=x{% endequation %} לכל {% equation %}x\in A{% endequation %}; זו אחת מהתכונות שמאפיינות פעולה של חבורה על קבוצה, שאיבר היחידה תמיד פועל בתור פונקציית הזהות. נראה שגם מתבקש שההופכי של {% equation %}\left(a,b\right){% endequation %} יהיה {% equation %}\left(a^{-1},b^{-1}\right){% endequation %} (זה הרי קורה במכפלה ישרה וזה גם הדבר המתבקש ממילא). האמנם? מה קורה אם כופלים אותם?

{% equation %}\left(a,b\right)\left(a^{-1},b^{-1}\right)=\left(a\left(b\cdot a^{-1}\right),bb^{-1}\right)=\left(a\left(b\cdot a^{-1}\right),e_{B}\right){% endequation %}

ובכן, האם {% equation %}a\left(b\cdot a^{-1}\right){% endequation %} הוא {% equation %}e_{A}{% endequation %}? לא. חסר לנו פה משהו. אם רק היינו יכולים לבטל את הפעולה של {% equation %}b{% endequation %} איכשהו! ובכן, אפשר: במקום לבחור בתור ההופכי את {% equation %}\left(a^{-1},b^{-1}\right){% endequation %} נבחר את {% equation %}\left(b^{-1}\cdot a^{-1},b^{-1}\right){% endequation %}. עכשיו נקבל

{% equation %}\left(a,b\right)\left(b^{-1}\cdot a^{-1},b^{-1}\right)=\left(a\left(b^{-1}b\cdot a^{-1}\right),bb^{-1}\right)=\left(aa^{-1},e_{B}\right)=\left(e_{A},e_{B}\right){% endequation %}

אבל יש עכשיו סוג של חוסר סימטריה בהגדרה שבגללו אני מרגיש צורך לוודא שגם כפל שבו הופכים את שני האיברים הללו נותן את אותה התוצאה:

{% equation %}\left(b^{-1}\cdot a^{-1},b^{-1}\right)\left(a,b\right)=\left(\left(b^{-1}\cdot a^{-1}\right)\left(b^{-1}\cdot a\right),b^{-1}b\right)={% endequation %}

{% equation %}=\left(b^{-1}\cdot\left(a^{-1}a\right),e_{B}\right)=\left(b^{-1}e_{A},e_{B}\right)=\left(e_{A},e_{B}\right){% endequation %}

כאשר שני המעברים האחרונים נובעים מכך שהפעולה של {% equation %}B{% endequation %} היא אוטומורפיזם.
<h2>מכפלה חצי ישרה חיצונית היא מכפלה חצי ישרה פנימית!</h2>
זה מסיים את הצגת המושג של מכפלה חצי ישרה חיצונית. עכשיו אני רוצה לשכנע אתכם שזה אותו מושג כמו מכפלה חצי ישרה פנימית. כלומר, שאפשר לראות את {% equation %}A\rtimes_{\varphi}B{% endequation %} גם בתור מכפלה חצי ישרה פנימית של שתי תתי חבורות - אלו שמתאימות בצורה הטריוויאלית ל-{% equation %}A,B{% endequation %}. אסמן אותן ב-{% equation %}H,K{% endequation %}. כלומר, אגדיר

{% equation %}H=\left\{ \left(a,e_{B}\right)\ |\ a\in A\right\} {% endequation %}

{% equation %}K=\left\{ \left(e_{A},b\right)\ |\ b\in B\right\} {% endequation %}

קל לראות ש-{% equation %}A\cong H{% endequation %} ו-{% equation %}B\cong K{% endequation %} אז אדלג על זה. יש שלושה דברים שאני כן רוצה להראות:
<ol>
	<li>{% equation %}H{% endequation %} <strong>נורמלית</strong> ב-{% equation %}A\rtimes_{\varphi}B{% endequation %}. זו אחת מהדרישות לכך שנוכל לדבר על המכפלה החצי ישרה הפנימית של {% equation %}H,K{% endequation %}.</li>
	<li>{% equation %}\left|H\cap K\right|=1{% endequation %} - זו עוד דרישה שבלעדיה ברור שהמכפלה הפנימית תהיה שונה מהחיצונית.</li>
	<li>לבסוף, החשוב ביותר - כשדיברנו על מכפלה פנימית, ה"פעולה" של {% equation %}K{% endequation %} על {% equation %}H{% endequation %} הייתה באמצעות <strong>הצמדה</strong>. במכפלה החיצונית של {% equation %}A,B{% endequation %} הפעולה הוגדרה באמצעות {% equation %}\varphi{% endequation %} שהתאימה לכל איבר של {% equation %}B{% endequation %} אוטומורפיזם של {% equation %}A{% endequation %}. מה שעלינו להראות הוא שלכל איבר {% equation %}b\in B{% endequation %}, האוטומורפיזם ש-{% equation %}\varphi{% endequation %} הצמידה לו הוא בדיוק מה שמוגדר על ידי הצמדה באמצעות {% equation %}\left(e_{A},b\right){% endequation %} (האיבר של {% equation %}K{% endequation %} שמתאים ל-{% equation %}b{% endequation %}). פורמלית, {% equation %}\left(b\cdot a,e_{B}\right)=\left(e_{A},b\right)\left(a,e_{B}\right)\left(e_{A},b\right)^{-1}{% endequation %}.</li>
</ol>
2 הוא מובן מאליו ונובע מההגדרה - האיבר המשותף היחיד הוא {% equation %}\left(e_{A},e_{B}\right){% endequation %}. בואו נעבור ל-3 דווקא, כי הוא כולל חישוב פשוט יחסית (הצמדה של איבר של {% equation %}H{% endequation %} עם מישהו מ-{% equation %}K{% endequation %}, להבדיל מהוכחה ש-{% equation %}H{% endequation %} נורמלית שתצריך אותי להצמיד עם איבר כלשהו). כאן אין חוכמות גדולות, פשוט כופלים את שלושת האיברים על פי כללי הכפל (ומכיוון שכבר ראינו שיש אסוציאטיביות, לא חשוב איזו משתי ההכפלות נבצע קודם):

{% equation %}\left(e_{A},b\right)\left(a,e_{B}\right)\left(e_{A},b\right)^{-1}=\left(e_{A}\left(b\cdot a\right),e_{B}b\right)=\left(e_{A},b\right)^{-1}{% endequation %}

{% equation %}\left(b\cdot a,b\right)\left(e_{A},b\right)^{-1}=\left(b\cdot a,b\right)\left(b^{-1}\cdot e_{A}^{-1},b^{-1}\right){% endequation %}

{% equation %}=\left(b\cdot a,b\right)\left(e_{A},b^{-1}\right)=\left(\left(b\cdot a\right)\left(b\cdot e_{A}\right),bb^{-1}\right){% endequation %}

{% equation %}=\left(b\cdot a,e_{B}\right){% endequation %}

וקיבלנו את המבוקש.

נשאר רק להראות ש-{% equation %}H{% endequation %} נורמלית. האינטואיציה פה היא שראינו שהצמדה על ידי איבר של {% equation %}K{% endequation %} משמרת את {% equation %}H{% endequation %}, ומן הסתם גם הצמדה על ידי איבר של {% equation %}H{% endequation %} תשמר את {% equation %}H{% endequation %}. עכשיו, אנחנו יודעים ש-{% equation %}HK{% endequation %} כוללת את <strong>כל</strong> אברי החבורה (זה נובע מתכונה 2), כלומר אפשר להציג כל איבר בחבורה בתור מכפלה של איבר מ-{% equation %}K{% endequation %} באיבר מ-{% equation %}H{% endequation %}. זה תרגיל קל להוכיח שהצמדה על ידי מכפלה של שני איברים שכל אחד מהם בנפרד משמר את {% equation %}H{% endequation %} עדיין משמרת את {% equation %}H{% endequation %}, מה שמסיים את ההוכחה.

ראינו כאן את הבניה הבסיסית האחרונה שאני רוצה להציג במסגרת סדרת הפוסטים שלי על חבורות. אבל מה עושים עם זה? אני מקווה לומר מילה וחצי על כך בהמשך.
