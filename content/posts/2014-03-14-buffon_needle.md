---
id: 3078
title: "המחט של בופון"
date: 2014-03-14 00:20:46
layout: post
categories: 
  - אנליזה מתמטית
  - מספרים
  - משחקים וחידות מתמטיות
tags: 
  - המחט של בופון
  - פאי
  - תוצאות לא אינטואיטיביות
social_media_share: true
---
היום חל "יום פאי", כלומר תאריך היום הוא ה-14/3, שבארצות פחות מתוקנות נכתב כ-3.14, כלומר כמו התחלת הפיתוח העשרוני של הקבוע {% equation %}\pi{% endequation %}, פאי (היחס בין היקף מעגל לקוטרו בגאומטריה האוקלידית) - ומכאן, תירוץ לחגוג ולאכול פאי עם פאי.

<strong><a href="{{site.baseurl}}{{site.post_images}}/2014/03/pi-pie.jpg"><img class="alignnone size-full wp-image-3079" alt="pi pie" src="{{site.baseurl}}{{site.post_images}}/2014/03/pi-pie.jpg" width="176" height="176" /></a></strong>

מבחינתי זה תירוץ לכתוב פוסט על משהו שבו מופיע {% equation %}\pi{% endequation %}, ורצוי משהו קליל יחסית. דוגמה נפלאה ל"משהו" כזה שטרם הופיע בבלוג בשום צורה היא בעיית המחט של בופון. בפשטות, הבעיה אומרת את הדבר הבא: יש לנו מחברת שורות ואנחנו זורקים עליה מחט. מה ההסתברות שהמחט תיפול על קו מפריד כלשהו במחברת?

ברור שהשאלה הזו תלויה בשני פרמטרים - אורך המחט, והרוחב של כל שורה (דהיינו, מה המרחק בין כל שני קווים מפרידים של שורות). נסמן את אורך המחט ב-{% equation %}l{% endequation %} ואת הרוחב של שורה ב-{% equation %}d{% endequation %}. בציור הבא אפשר לראות את השורות ברוחב {% equation %}d{% endequation %} ושני מחטים באורך {% equation %}l{% endequation %}, שאחת מהן לא נפלה על אף קו מפריד, ואחת כן נפלה:

<strong><a href="{{site.baseurl}}{{site.post_images}}/2014/03/needles1.png"><img class="alignnone size-full wp-image-3080" alt="needles1" src="{{site.baseurl}}{{site.post_images}}/2014/03/needles1.png" width="811" height="399" /></a></strong>

קל להגיע למסקנה שיש הבדל כלשהו בין הסיטואציה שבה {% equation %}l>d{% endequation %}, כלומר המחט גדולה מרוחב שורה ולכן אם היא נופלת בזווית שמאונכת לקווים המפרידים היא על בטוח חוצה קו מפריד שכזה, ובין הסיטואציה שבה {% equation %}l\le d{% endequation %}. אני הולך לדבר <strong>רק</strong> על הסיטואציה השניה, מהטעם הפשוט שהנוסחה יוצאת הרבה יותר פשוטה ונחמדה בה, והרעיון עבור {% equation %}l>d{% endequation %} הוא אותו רעיון, עם עוד פרטים טכניים.

איך זה קשור לפאי? פשוט מאוד - התשובה הולכת לערב את פאי איכשהו, למרות שאין לו רמז בניסוח השאלה, ואפילו אין בשאלה מעגלים (מעגלים הם המקור הטבעי לפאי). אז מאיפה פאי הגיע? נראה די מהר שבאופן די טבעי אפשר לערב מעגלים בשאלה ואפילו כדאי, ושפאי מגיע מהם.

אני רוצה להראות בפוסט הזה שני פתרונות לבעיה. הראשון יהיה שימוש סטנדרטי בחשבון אינפיניטסימלי - מסוג הדברים שסביר לתת לסטודנטים להסתברות לעשות. במילים אחרות, זה יהיה פתרון נכון ופשוט, אבל הוא לא יהיה כל כך <strong>מעניין</strong>. הפתרון השני הוא מגניב משמעותית מהראשון וגם נלמד עוד דברים מתוך ההוכחה שלו, אבל אני מעדיף "להוציא מהמערכת" את הפתרון הסטנדרטי קודם כל. למי שלא מתעניין בפתרון הזה או שהפרטים הטכניים מרתיעים אותו - פשוט תקפצו מעליו, לא אכפת לי. אני אשב עם האינטגרל שלי לבד, בחושך. הכל בסדר.

אוקיי, אז מה עושים? ראשית כל צריך לחדד עניינים כמו מה מרחב ההסתברות שלנו וכדומה. כשאנחנו "זורקים" מחט, מה אנחנו בעצם מגרילים? שני דברים - את ה<strong>זווית</strong> שלה (ביחס לציר {% equation %}x{% endequation %}, כפי שבדרך כלל מחשבים זווית של ישרים) ואת ה<strong>מיקום</strong> שלה. אני אסתכל על אחת מהקצוות של המחט בתור ה"ראשית" שלה, והמיקום של המחט יהיה המיקום של הראשית הזו. הזווית תימדד ביחס לסיבוב שבו משאירים את הראשית קבועה (כלומר, מסובבים את המחט סביב הראשית ובודקים כמה סיבוב עם כיוון השעון נדרש כדי "להחזיר" אותה למצב שבו היא מתלכדת עם ציר {% equation %}x{% endequation %}). לא קשה לראות שהמיקום ה<strong>אופקי</strong> של המחט, או השאלה באיזו שורה במחברת הראשית של המחט נפלה, הן חסרות חשיבות - כל מה שחשוב הוא הזווית, שהיא מספר {% equation %}0\le\theta\le2\pi{% endequation %} (הנה פאי!) והגובה של הראשית מעל הקו המפריד התחתון בשורה, {% equation %}0\le h\le d{% endequation %}. הנה ציור שמבהיר את זה:

<strong><a href="{{site.baseurl}}{{site.post_images}}/2014/03/needles2.png"><img class="alignnone size-full wp-image-3081" alt="needles2" src="{{site.baseurl}}{{site.post_images}}/2014/03/needles2.png" width="811" height="204" /></a></strong>

המספרים {% equation %}\theta,h{% endequation %} הללו נבחרים בהתפלגות אחידה מתוך התחומים שלהם. לכן (מנימוקים סטנדרטיים בהסתברות), ההסתברות שהמחט תחצה קו מפריד היא בדיוק היחס בין שטח של קבוצת כל הנקודות {% equation %}\left(\theta,h\right){% endequation %} שעבורן המחט חוצה קו מפריד ובין השטח של כל הנקודות {% equation %}\left(\theta,h\right){% endequation %} הרלוונטיות בכלל. אם כן, נשאלת השאלה: בהינתן {% equation %}\theta{% endequation %}, מה הערכים של {% equation %}h{% endequation %} שעבורם יש חצייה?

ובכן, בהינתן {% equation %}\theta,h{% endequation %}, השאלה היא מה גובה הקצה של המחט שאינו הראשית. התשובה היא שימוש סטנדרטי בטריגונומטריה: {% equation %}h+l\sin\theta{% endequation %}.

כאשר {% equation %}\theta>\pi{% endequation %} הגובה הוא <strong>נמוך יותר</strong> מאשר {% equation %}h{% endequation %}. כדי לחסוך לעצמי פירוק למקרים, פשוט אצביע על כך שהמקרה הזה סימטרי למקרה של {% equation %}0\le\theta\le\pi{% endequation %} ולכן מעכשיו אסתפק בהנחה ש-{% equation %}0\le\theta\le\pi{% endequation %}. במקרה זה, על מנת שהמחט תחצה קו מפריד, צריך להתקיים {% equation %}h+l\sin\theta>d{% endequation %} (אגב, כל הדיבורים על "לחצות" את הקו המפריד מיותרים - גם אם נרשה למחט לגעת בלי לחצות החישובים שלנו לא ישתנו, מכיווון שההסתברות של כל מאורעות ה"נגיעה" הללו היא אפס - אין להם "שטח" - אבל נעזוב את זה). במילים אחרות, צריך להתקיים {% equation %}h>d-l\sin\theta{% endequation %}. מכאן אנחנו מקבלים את החישוב הבא של שטח קבוצת כל הנקודות שעבורן יש חציה:

{% equation %}\int_{0}^{\pi}\left(\int_{d-l\sin\theta}^{d}dh\right)d\theta=\int_{0}^{\pi}\left(d-\left(d-l\sin\theta\right)\right)d\theta=l\int_{0}^{\pi}\sin\theta d\theta=l\left(-\cos\pi+\cos0\right)=2l{% endequation %}

והשטח של קבוצת כל הנקודות הרלווניטות הוא שטח המלבן שאורכי צלעותיו {% equation %}\pi{% endequation %} ו-{% equation %}d{% endequation %}, כלומר {% equation %}d\pi{% endequation %}. בסך הכל אנחנו מקבלים את הנוסחה {% equation %}\frac{2}{\pi}\frac{l}{d}{% endequation %} - וזו אכן הנוסחה הנכונה. לא קשה לראות שהחישוב הזה נשבר אם {% equation %}d<l{% endequation %} וזה תרגיל טוב למצוא את הנוסחה במקרה הזה, אבל היא יוצאת מזעזעת, כאמור, וחבל.

אוקיי, אז סיימנו עם הפתרון הפשוט, ועכשיו אפשר לדבר בשקט על הפתרון המסובך בלי שאף אחד מהקהל יציץ וישאל "אבל למה לא פתרת עם אינטגרלים וזהו?!". אני רוצה לפתור בלי אינטגרלים כי הפתרון המסורבל יותר הוא פשוט יותר יפה ומהנה.

לפני שאציג אותו, קוריוז חביב שקשור לנוסחה שכבר מצאנו. כפי שאנחנו רואים, {% equation %}\pi{% endequation %} נמצא בנוסחה הזו בצורה פשוטה מאוד. זה מצביע על כך שאם נצליח, עבור {% equation %}l,d{% endequation %} נתונים, לחשב מספרית את ההסתברות לכך שהסיכה תחצה קו, נוכל לקבל מכך קירוב של פאי. איך אפשר לבצע את החישוב הזה? ובכן, פשוט תזרקו סיכות ותראו מה קורה! לטכניקת חישוב הסתברותית שכזו קוראים "שיטת מונטה-קרלו" (אין שיטה <strong>ספציפית</strong> שנקראת "מונטה-קרלו"; זה שם כללי להרבה שיטות חישוב שונות). בשנת 1901, מתמטיקאי בשם לזאריני טען שהוא באמת עשה את זה - השליך סיכות על מחברת וספר בכמה פעמים הסיכה נפלה על הקו. הוא זרק 3408 סיכות, כך ש-{% equation %}\frac{l}{d}{% endequation %} היה {% equation %}\frac{5}{6}{% endequation %}, ומצא שבדיוק ב-1808 מהפעמים הסיכות נפלו על הקו. אז מה הקירוב של פאי שנקבל כאן? {% equation %}\frac{2}{\pi}\frac{5}{6}\approx\frac{1808}{3408}{% endequation %}, כלומר

{% equation %}\pi\approx\frac{10}{6}\cdot\frac{3408}{1808}=\frac{355}{113}=3.1415929\dots{% endequation %}

זה קירוב די פנטסטי. למעשה, פנטסטי <strong>מדי</strong>. {% equation %}\frac{355}{113}{% endequation %} הוא הקירוב הטוב ביותר לפאי באמצעות מספר רציונלי עם מונה ומכנה קטנים (הקירוב המפורסם האחר הוא {% equation %}\frac{22}{7}{% endequation %} שגם הוא מצויין אבל פחות טוב). זה מתחיל להסביר לנו למה לזאריני הטיל סיכה בדיוק 3408 פעמים - מספר מוזר ולא עגול לכל הדעות - ולמה הוא בחר את {% equation %}l,d{% endequation %} בצורה שנותנת {% equation %}\frac{l}{d}=\frac{5}{6}{% endequation %} הוא ניסה להנדס את הקירוב {% equation %}\frac{355}{113}{% endequation %}!

בואו נראה את זה מתמטית. אם {% equation %}p{% endequation %} היא ההסתברות להפיל מחט על קו מפריד, אז {% equation %}\frac{2}{\pi}\frac{l}{d}=p{% endequation %}, כלומר {% equation %}\pi=\frac{2}{p}\frac{l}{d}{% endequation %}. אם אנחנו רוצים לקבל את הקירוב {% equation %}\pi\approx\frac{355}{113}{% endequation %}, אנחנו צריכים שיתקיים {% equation %}\frac{355}{113}=\frac{2l}{d}\cdot\frac{T}{a}{% endequation %}, כאשר {% equation %}T{% endequation %} הוא מספר הנסיונות הכולל שלנו ו-{% equation %}a{% endequation %} הוא מספר ההצלחות. עכשיו, מספר ההצלחות הוא תמיד מספר שלם, וצריך להתקיים {% equation %}a=\frac{113}{355}\cdot\frac{2l}{d}T{% endequation %} - שוויון ממש! במילים אחרות, הסיכוי לקבל את הקירוב הנפלא הזה ל-{% equation %}\pi{% endequation %} הוא רק אם {% equation %}a{% endequation %} יוצא "בסדר" כאשר {% equation %}T{% endequation %} כפול {% equation %}\frac{113}{355}\cdot\frac{2l}{d}{% endequation %} יוצא מספר שלם. לכן, אם לזאריני רוצה לעבוד כמה שפחות קשה, הוא רוצה לבחור את {% equation %}\frac{113}{355}\cdot\frac{2l}{d}{% endequation %} בצורה שבה המכנה יהיה קטן. {% equation %}355=5\cdot71{% endequation %} ולכן מתבקש לבחור {% equation %}l=5{% endequation %} כדי לנטרל את ה-5 שב-355. נקבל {% equation %}\frac{113}{71}\cdot\frac{2}{d}{% endequation %}. אנחנו חייבים לבחור את {% equation %}d{% endequation %} להיות גדול מ-{% equation %}l{% endequation %}, וככל שהוא יותר גדול כך זה מקשה עלינו יותר, אז נבחר {% equation %}d=6{% endequation %} ונקל {% equation %}\frac{113}{71}\cdot\frac{1}{3}=\frac{113}{213}{% endequation %}.

מה יוצא מכל זה בפועל? שעל כל 213 השלכות סיכה שלזאריני מבצע, יש לו סיכוי לקבל את הקירוב הנפלא {% equation %}\frac{355}{113}{% endequation %} לפאי, אם רק יתמזל מזלו ויתקיים שב-{% equation %}T{% endequation %} השלכות הסיבה שבוצעו עד כה, בדיוק {% equation %}\frac{113}{213}T{% endequation %} מההשלכות נפלו על הקו. כעת, {% equation %}\frac{3408}{213}=16{% endequation %}, כלומר ללזאריני היו 16 "הזדמנויות" כאלו לפני שהוא קיבל את מבוקשו, ואז הפסיק מייד (כל השלכה נוספת הייתה מקלקלת לו את הקירוב הנפלא). זה כמובן מסביר את המספר המוזר והלא עגול {% equation %}3408{% endequation %} ואת הבחירה של {% equation %}l,d{% endequation %}. לטעמי לזאריני אמנם יצא רמאי, אבל רמאי משעשע והניתוח של הרמאות שלו הוא מהנה, אז אני שמח שהוא רימה ככה.

כעת בואו נעבור לפתרון היפה יותר לבעיית המחט. הרעיון הוא לפתור בעיה כללית יותר: אנחנו זורקים מחט מאורך {% equation %}l{% endequation %} <strong>כלשהו</strong> (גם {% equation %}l>d{% endequation %}) בצורה אקראית ושואלים <strong>כמה</strong> קווים המחט הולכת לחתוך. במילים אחרות, אנחנו מגדירים משתנה מקרי {% equation %}X{% endequation %} שסופר את החיתוכים של המחט עם הקווים המפרידים, ותוהים מה ה<strong><a href="http://www.gadial.net/2010/08/14/random_variables/">תוחלת</a> </strong>של המשתנה הזה, {% equation %}E\left[X\right]{% endequation %}. פתרון כללי לשאלה הזו נותן גם פתרון כללי לשאלת ההסתברות במקרה של {% equation %}l<d{% endequation %}, מכיוון שאז מספר החיתוכים הוא או 1 או 0, כלומר המשתנה המקרי הוא מה שנקרא <strong>אינדיקטור</strong> והתוחלת שלו שווה להסתברות שהוא יקבל 1.

ולמה כל כך מועיל לעבור לדבר על תוחלת? בגלל שיש לתוחלת תכונה נפלאה, קסם של ממש, שנקראת <strong>לינאריות</strong>. אם {% equation %}X,Y{% endequation %} הם שני משתנים מקריים, אז מתקיים {% equation %}E\left[X+Y\right]=E\left[X\right]+E\left[Y\right]{% endequation %}, וזה נכון <strong>גם אם המשתנים תלויים הסתברותית</strong>.

איך ננצל את תכונת התוחלת הזו? על ידי התעלול הבא: נניח שאנחנו זורקים מחט באורך {% equation %}l{% endequation %} באקראי, אבל חושבים על המחט בתור <strong>שתי</strong> מחטים ש"הודבקו" אחת לשניה - מחט אחת מאורך {% equation %}x{% endequation %} והמחט השניה מאורך {% equation %}y{% endequation %}. אז {% equation %}E\left[l\right]=E\left[x+y\right]=E\left[x\right]+E\left[y\right]{% endequation %} (כאן אני עושה מה שמכונה Abuse of notation - אני כותב את אורכי המחטים במקום לטרוח ולכתוב שמות של משתנים מקריים שמייצגים את המחטים מהאורך הזה).

אז מה קיבלנו? תשכחו לשניה מהסתברות ותוחלות וכאלה. יש לנו פונקציה {% equation %}f{% endequation %} שמוגדרת על כל הממשיים החיוביים, ומקיימת {% equation %}f\left(x+y\right)=f\left(x\right)+f\left(y\right){% endequation %}. משוואה כזו נקראת <strong>משוואה פונקציונלית</strong>, כי הנעלם בה הוא בכלל {% equation %}f{% endequation %} - אנחנו מבקשים לדעת אילו פונקציות {% equation %}f{% endequation %} הן פתרון למשוואה הזו. המשוואה הספציפית הזו היא מפורסמת - היא נקראת "המשוואה הפונקציונלית של קושי". בעבר כבר <a href="http://www.gadial.net/2010/03/27/exponent/">הראיתי בבלוג</a> איך פותרים משוואה פונקציונלית דומה ("המשוואה הפונקציונלית האקספוננציאלית של קושי), המשוואה {% equation %}f\left(x+y\right)=f\left(x\right)\cdot f\left(y\right){% endequation %}. טכניקת הפתרון כאן היא דומה:

ראשית, שימו לב לכך ש-{% equation %}f\left(2x\right)=f\left(x\right)+f\left(x\right)=2f\left(x\right){% endequation %}. כעת תעשו אותו דבר עם {% equation %}n{% endequation %} עותקים של {% equation %}x{% endequation %} ותקבלו {% equation %}f\left(nx\right)=nf\left(x\right){% endequation %} לכל {% equation %}n{% endequation %} טבעי (אפשר להוכיח פורמלית באינדוקציה). השלב הבא הוא לשים לב לכך ש-{% equation %}f\left(x\right)=f\left(\frac{x}{m}+\dots+\frac{x}{m}\right)=mf\left(\frac{x}{m}\right){% endequation %}, אז קיבלנו {% equation %}f\left(\frac{x}{m}\right)=\frac{1}{m}f\left(x\right){% endequation %}. על כן, {% equation %}f\left(\frac{n}{m}x\right)=nf\left(\frac{1}{m}x\right)=\frac{n}{m}f\left(x\right){% endequation %}, או במילים אחרות - {% equation %}f\left(rx\right)=rf\left(x\right){% endequation %} לכל {% equation %}r{% endequation %} רציונלי. אם נסמן {% equation %}f\left(1\right)=c{% endequation %}, אז קיבלנו {% equation %}f\left(r\right)=f\left(1\cdot r\right)=rf\left(1\right)=cr{% endequation %} לכל {% equation %}r{% endequation %} רציונלי. מה קורה עם מספרים אי רציונליים? באופן כללי צריך עוד הנחה על האופי של {% equation %}f{% endequation %}.

במקרה שלנו אנחנו יודעים ש-{% equation %}f{% endequation %} היא <strong>מונוטונית</strong>, כלומר מקיימת שאם {% equation %}x<y{% endequation %} אז {% equation %}f\left(x\right)\le f\left(y\right){% endequation %} (למה? כי במקרה שלנו, אם {% equation %}x<y{% endequation %} אז {% equation %}y=x+z{% endequation %} כאשר גם {% equation %}z{% endequation %} חיובי, ואז {% equation %}E\left[y\right]=E\left[x+y\right]=E\left[x\right]+E\left[z\right]\ge E\left[x\right]{% endequation %}). זה מסיים את הסיפור לכל {% equation %}x{% endequation %} ממשי ומוכיח ש-{% equation %}f\left(x\right)=cx{% endequation %}. שכן אפשר לקחת שני רציונליים {% equation %}r_{1},r_{2}{% endequation %} כך ש-{% equation %}r_{1}&lt;x&lt;r_{2}{% endequation %} והם קרובים ל-{% equation %}x{% endequation %} כרצוננו, ויתקיים {% equation %}f\left(r_{1}\right)\le f\left(x\right)\le f\left(r_{2}\right){% endequation %}, דהיינו {% equation %}cr_{1}\le f\left(x\right)\le cr_{2}{% endequation %}. כאשר {% equation %}r_{1}{% endequation %} ו-{% equation %}r_{2}{% endequation %} שואפים ל-{% equation %}x{% endequation %}, הביטויים משמאל ומימין שואפים ל-{% equation %}cx{% endequation %} ולכן הפונקציה באמצע שואפת ל-{% equation %}cx{% endequation %} גם כן ("כלל הסנדוויץ'").

אם לחזור למחט של בופון, קיבלנו ש-{% equation %}E\left[l\right]=c\cdot l{% endequation %}. רק נותר להבין מיהו {% equation %}c{% endequation %} המדובר. אנחנו כבר יודעים שהוא אמור להיות {% equation %}c=\frac{2}{\pi d}{% endequation %}, אבל איך מגיעים אל זה?

כאן מגיע הקסם הנפלא, שבזכותו ההוכחה הזו כל כך אדירה. כבר ראינו קודם שמחט ארוכה אפשר לקחת ולחשוב עליה כעל שתי מחטים קטנות יותר "דבוקות" זו לזו - כל מה שחשוב הוא שסכום אורכי המחטים הוא אורך המחט המקורית. הנקודה היא שאפשר לעשות את זה גם בצורה קיצונית יותר - גם אם המחט שלנו היא <strong>לא קו ישר</strong> אלא אוסף של קווים ישרים מחוברים - "עקום פוליגונלי". למשל זה:

<a href="{{site.baseurl}}{{site.post_images}}/2014/03/needles3.png"><img class="alignnone size-full wp-image-3082" alt="needles3" src="{{site.baseurl}}{{site.post_images}}/2014/03/needles3.png" width="811" height="267" /></a>

זה לא משנה איך ה"מחטים" שמהם מורכב העקום מחוברות זו לזו - כל מה שחשוב הוא סכומי האורכים שלהן. אפשר לחשוב על ניסוי השלכת הצורה הפוליגונלית על המחברת בתור אוסף של השלכות של כל המחטים האינדיבידואליות; כמובן, בגלל שהמחטים דבוקות זו לזו אז הניסויים הללו תלויים מבחינה הסתברותית, אבל כבר אמרתי שהקטע עם "התוחלת היא סכום התוחלות" <strong>לא מושפע</strong> מזה.

ועכשיו הפאנץ': בואו ניקח בתור ה"מחט" שלנו <strong>מעגל</strong>. כמובן, מעגל הוא לא עקום פוליגונלי, אבל אפשר לקרב אותו כרצוננו עם עקומים פוליגונליים כך שכדי להוכיח את מה שאטען כרגע על מעגל רק צריך עוד קצת ביסוס טכני שלא אכנס אליו (הוא תרגיל מצויין כדי לוודא שהבנתם מה קורה פה). אז חזרה למעגל - אני אקח מעגל שקוטרו הוא בדיוק {% equation %}d{% endequation %}. מעגל כזה, לא משנה איך תשימו אותו, הולך להכיל בדיוק שני חיתוכים עם קווים מפרידים (שוב, ייתכן שהוא רק ישיק לשניהם, אבל זה מקרה עם הסתברות 0 ואפשר גם לדבר על "נגיעה בקווים מפרידים" במקום "חיתוך" אם זה מפריע למישהו). הנה, תראו הוכחה על ידי תמונה:

<strong><a href="{{site.baseurl}}{{site.post_images}}/2014/03/needles4.png"><img class="alignnone size-full wp-image-3083" alt="needles4" src="{{site.baseurl}}{{site.post_images}}/2014/03/needles4.png" width="820" height="381" /></a></strong>

אם כן, אנחנו יודעים שעבור {% equation %}l=\pi d{% endequation %} (היקף מעגל שקוטרו {% equation %}d{% endequation %}, כמובן) מתקיים {% equation %}E\left[\pi d\right]=c\pi d=2{% endequation %}, כלומר {% equation %}c=\frac{2}{\pi d}{% endequation %} וסיימנו. לא יודע מה איתכם, אותי הטיעון הזה, עם המעגל שבא משום מקום, פשוט הפיל לקרקע מרוב שהוא אדיר.

מי שהמציא/גילה את ההוכחה הנפלאה הזו הוא המתמטיקאי הצרפתי Joseph-Émile Barbier. אבל הוא לא עצר כאן - למעשה, מה שעשינו כאן הוא הוכחה לתוצאה עוד יותר מעניינת, שמושגת כאשר הופכים את מה שעשינו כאן על פיו. לצורך כך, בואו נאמר שצורה קמורה היא בעלת <strong>רוחב קבוע</strong> {% equation %}d{% endequation %} אם לכל שני קווים מקבילים שמשיקים לצורה, המרחק ביניהם הוא {% equation %}d{% endequation %}. מעגל הוא בבירור צורה כזו, עם רוחב ששווה לקוטר שלה, אבל יש עוד צורות, למשל "<a href="http://en.wikipedia.org/wiki/Reuleaux_triangle">משולש רולו</a>":

<strong><a href="{{site.baseurl}}{{site.post_images}}/2014/03/triangle.jpg"><img class="alignnone size-full wp-image-3084" alt="triangle" src="{{site.baseurl}}{{site.post_images}}/2014/03/triangle.jpg" width="160" height="160" /></a></strong>

כעת, בהוכחה של הנוסחה עבור המחט של בופון השתמשנו במעגל עם קוטר {% equation %}d{% endequation %} כי זו צורה פשוטה ונחמדה, אבל <strong>כל צורה קמורה</strong> עם רוחב קבוע {% equation %}d{% endequation %} הייתה עובדת באותה המידה. הרוחב הקבוע אומר שלא משנה איך נשליך אותה על המחברת שלנו (כלומר, איך "סובבנו" אותה), או ששני קווי גבול במחברת ישיקו לה, או שבדיוק קו גבול אחד יעבור דרכה - ומכיוון שהיא קמורה, המשמעות היא שהוא יחתוך אותה בדיוק בשתי נקודות (לצורות לא קמורות זה לא עובד).

אם כן, ניקח צורה קמורה כלשהי מרוחב קבוע {% equation %}d{% endequation %} ועם היקף {% equation %}l{% endequation %}. תוחלת מספר החיתוכים כשמשליכים אותה על המחברת הוא מצד אחד 2 מהסיבה שפירטתי כרגע, ומצד שני על פי הנוסחה הוא {% equation %}\frac{2l}{\pi d}{% endequation %}. מסקנה: {% equation %}\frac{2l}{\pi d}=2{% endequation %}, או {% equation %}l=\pi d{% endequation %}. כלומר, ההיקף של הצורה הוא <strong>תמיד</strong> {% equation %}\pi d{% endequation %}, בין אם היא מעגל ובין אם לאו. להציב {% equation %}d=1{% endequation %} נותן את התוצאה הזו בצורה אפילו יותר ברורה, למי שפספס אותי לרגע:

כל צורה קמורה בעלת רוחב קבוע 1 היא בעלת היקף {% equation %}\pi{% endequation %}.

לא רק מעגלים.

את יום פאי הבא נחגוג עם פאי בצורת משולש רולו?

