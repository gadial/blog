---
id: 2349
title: "הבעיה העשירית של הילברט - לכל דבר טוב (חסום) יש סוף"
date: 2013-02-02 10:37:57
layout: post
categories: 
  - תורת המספרים
tags: 
  - הבעיה העשירית של הילברט
---
בשעה טובה הגענו אל המכשול האחרון שעומד בינינו ובין סיום ההוכחה שהבעיה העשירית של הילברט אינה כריעה - כמת אוניברסלי חסום. אם נצליח להראות שבהינתן ביטוי דיופנטי {% equation %}P{% endequation %} אפשר להוכיח שגם הביטוי {% equation %}\forall x&lt;n\left(P\right){% endequation %} הוא דיופנטי, נסיים. כאן אמורה להיכנס לתמונה העובדה שהוכחנו (בדם יזע ודמעות) שהפונקציה האקספוננציאלית היא דיופנטית. בואו נתחיל בלראות עבור עוד פונקציות שגדלות בקצב מהיר שהן דיופנטיות.

נפתח בפונקציה שהיא אקספוננציאלית-כפולה: {% equation %}h\left(u,v,w\right)=u^{v^{w}}{% endequation %}. בהינתן שהפונקציה האקספוננציאלית היא דיופנטית, קל לבנות ביטוי עבור הפונקציה הזו:

{% equation %}y=u^{v^{w}}\iff\exists z\left(y=u^{z}\wedge z=v^{w}\right){% endequation %}

דהיינו, אנחנו עושים שימוש כפול במערכות המשוואות עבור הפונקציה האקספוננציאלית, כל פעם עם משתנים אחרים.

זו הייתה פונקציה קלה, בואו נדבר על משהו מסובך יותר - מקדמי הבינום, {% equation %}f\left(n,k\right)={n \choose k}{% endequation %}. כדי לטפל בהם, קודם כל נוכיח את הזהות {% equation %}\sum_{i=k}^{n}{n \choose i}u^{i-k}=\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]{% endequation %} שמתקיימת עבור {% equation %}0&lt;k\le n{% endequation %} ו-{% equation %}u&gt;2^{n}{% endequation %} (והוא מספר טבעי), כאשר סוגריים מרובעים מסמנים ערך שלם תחתון (המספר השלם הגדול ביותר שקטן או שווה למה שבתוך הסוגריים).

אני מניח שלפחות חלקכם משער שהדרך הנכונה להתחיל הוכחה כזו היא עם נוסחת הביטום של ניוטון, שמתארת את הסכום כש-{% equation %}k{% endequation %} מתחיל מ-0: {% equation %}\sum_{i=0}^{n}{n \choose i}u^{i}=\left(u+1\right)^{n}{% endequation %}. כעת, נחלק את שני האגפים ב-{% equation %}u^{k}{% endequation %} (מתבקש לגמרי, נכון?) ונקבל {% equation %}\sum_{i=0}^{n}{n \choose i}u^{i-k}=\frac{\left(u+1\right)^{n}}{u^{k}}{% endequation %}. את הסכום שבאגף שמאל אפשר לחלק לשני סכומים שונים: {% equation %}\sum_{i=0}^{k-1}{n \choose i}u^{i-k}+\sum_{i=k}^{n}{n \choose i}u^{i-k}{% endequation %}. מביניהם, הימני הוא הסכום שאנו רוצים לחשב, והשמאלי הוא סתם שארית מעצבנת. מה שאנחנו רוצים לומר הוא שכאשר לוקחים ערך שלם תחתון על שני הסכומים הללו, הסכום השמאלי פשוט מתפוגג לו. מכיוון שהסכום הימני הוא מספר שלם, מספיק להראות ש-{% equation %}\sum_{i=0}^{k-1}{n \choose i}u^{i-k}&lt;1{% endequation %} כדי להוכיח שהערך השלם התחתון יעלים אותו.

כעת, {% equation %}u{% endequation %} הוא מספר טבעי, כלומר {% equation %}u^{i+1-k}\le1{% endequation %} לכל {% equation %}0\le i&lt;k{% endequation %}, כלומר (נחלק ב-{% equation %}u{% endequation %} את שני האגפים) לכל {% equation %}i&lt;k{% endequation %} אנו מקבלים {% equation %}u^{i-k}\le u^{-1}{% endequation %}. מכאן שאפשר לחסום את הסכום בצורה הבאה:

{% equation %}\sum_{i=0}^{k-1}{n \choose i}u^{i-k}\le u^{-1}\sum_{i=0}^{k-1}{n \choose i}&lt;u^{-1}\sum_{i=0}^{n}{n \choose i}=u^{-1}2^{n}&lt;1{% endequation %}

וכאן אנחנו משתמשים בהנחה שלנו ש-{% equation %}u&gt;2^{n}{% endequation %} (וכמובן, בכך שעל פי הבינום של ניוטון, {% equation %}\sum_{i=0}^{n}{n \choose i}=\left(1+1\right)^{n}{% endequation %}).

שימו לב למסקנה הפשוטה מהזהות {% equation %}\sum_{i=k}^{n}{n \choose i}u^{i-k}=\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]{% endequation %} - אם ניקח את המשוואה הזו ונתבונן עליה מודולו {% equation %}u{% endequation %}, נקבל {% equation %}{n \choose k}\equiv_{u}\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]{% endequation %}, כי כל שאר המחוברים מתאפסים כשמסתכלים על המשוואה מודולו {% equation %}u{% endequation %}. זה התעלול שיאפשר לנו להגדיר את {% equation %}{n \choose k}{% endequation %} דיופנטית. מה שמעניין במשוואה הזו היא שאגף שמאל <strong>לא כולל </strong>את {% equation %}u{% endequation %}. מה שראינו הוא ש<strong>לכל</strong> {% equation %}u&gt;2^{n}{% endequation %} מתקיים ש-{% equation %}\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]{% endequation %} שקול מודולו {% equation %}u{% endequation %} ל-{% equation %}{n \choose k}{% endequation %}. כעת, {% equation %}{n \choose k}&lt;2^{n}&lt;u{% endequation %} ולכן זו יותר מסתם שקילות - זה מה שמתקבל כשלוקחים את {% equation %}\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]{% endequation %}, מחלקים ב-{% equation %}u{% endequation %} ובודקים מה השארית (נסו לחשב בעצמכם - במחשב - כמה מקרים אם אינכם מאמינים). זה מאפשר לנו להגדיר את {% equation %}{n \choose k}{% endequation %} באמצעות הביטוי הדיופנטי הבא:

{% equation %}z={n \choose k}\iff\exists u,v,w\left(v=2^{n}\wedge u&gt;v\wedge w=\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]\wedge z\equiv_{u}w\wedge z&lt;u\right){% endequation %}

יש כאן כמה וכמה רכיבים בתוך הסוגריים שצריך להשתכנע שכל אחד מהם לכשעצמו הוא דיופנטי. אז ראשית, {% equation %}v=2^{n}{% endequation %} הוא דיופנטי כי הפונקציה האקספוננציאלית היא דיופנטית (לכן נזקקנו לה). הביטוי {% equation %}u&gt;v{% endequation %} הוא בבירור דיופנטי (ראינו את זה בעבר - נסו לשחזר מהראש). כנ"ל {% equation %}z&lt;u{% endequation %}. הביטוי {% equation %}z\equiv_{u}w{% endequation %} אולי נראה טיפה יותר טריקי, אבל הוא שקול ל-{% equation %}\exists a\left(z=ua+w\right){% endequation %} הדיופנטי. מי נשאר? רק {% equation %}w=\left[\frac{\left(u+1\right)^{n}}{u^{k}}\right]{% endequation %} המפחיד. האתגר הוא בעצם להראות ש-{% equation %}w=\left[\frac{x}{y}\right]{% endequation %} הוא דיופנטי, כי {% equation %}\left(u+1\right)^{n}{% endequation %} ו-{% equation %}u^{k}{% endequation %} הן פונקציות אקספוננציאליות ולכן דיופנטיות. למרבה המזל, מכיוון שאי-שוויונים הם דיופנטיים, קל לתאר גם את {% equation %}w=\left[\frac{x}{y}\right]{% endequation %}: הרי אם {% equation %}w=\left[\frac{x}{y}\right]{% endequation %} זה אומר ש-{% equation %}w\le\frac{x}{y}\le w+1{% endequation %} ולכן {% equation %}yw\le x\wedge x\le y\left(w+1\right){% endequation %}, ושתי המשוואות הללו מספיקות. מסקנה סופית: {% equation %}{n \choose k}{% endequation %} היא דיופנטית (בזכות העובדה שהפונקציה האקספוננציאלית היא דיופנטית).

בואו נעבור עכשיו לתקוף פונקציה מפורסמת אחרת שגדלה מהר: {% equation %}f\left(n\right)=n!{% endequation %}. גם כאן כדי לתקוף אותה אנחנו צריכים משוואה אלגברית נחמדה כלשהי שהיא מקיימת; במקרה שלנו, אם {% equation %}u&gt;\left(2n\right)^{n+1}{% endequation %} אז {% equation %}n!=\left[u^{n}/{u \choose n}\right]{% endequation %} היא המשוואה המדוברת. שימו לב שזה משהו בסגנון דומה להוכחה הקודמת; גם פה אנחנו משתמשים בכך שאם אנחנו לוקחים שתי פונקציות שגדלות מהר עם בסיס כלשהו שמסומן ב-{% equation %}u{% endequation %} שהוא גדול דיו, אז מקבלים קירוב רציונלי די טוב לפונקציה שאנחנו רוצים לתקוף. כמו קודם, בואו ננסה להבין מהו {% equation %}u^{n}/{u \choose n}{% endequation %} עבור {% equation %}u{% endequation %} גדול שכזה:

{% equation %}u^{n}/{u \choose n}=u^{n}\cdot\frac{n!\left(u-n\right)!}{u!}=\frac{u^{n}n!}{u\left(u-1\right)\left(u-2\right)\cdots\left(u-n+1\right)}=n!\left(\frac{1}{1\left(1-\frac{1}{u}\right)\cdots\left(1-\frac{n-1}{u}\right)}\right){% endequation %}

כל מה שהלך כאן הוא אלגברה בסיסית. הביטוי האחרון נראה קצת מבהיל אולי, אבל עם אי שוויון אפשר להיפטר ממנו די בקלות:

{% equation %}n!\left(\frac{1}{1\left(1-\frac{1}{u}\right)\cdots\left(1-\frac{n-1}{u}\right)}\right)&lt;n!\frac{1}{\left(1-\frac{n}{u}\right)^{n}}{% endequation %}

זאת כי ככל שמגדילים את הערך של {% equation %}x{% endequation %} בביטוי {% equation %}\left(1-\frac{x}{u}\right){% endequation %} כך מקטינים את הביטוי, ולכן מגדילים את אחד חלקי הביטוי.

עכשיו, {% equation %}\frac{1}{\left(1-\frac{n}{u}\right)^{n}}=\left(\frac{1}{1-\frac{n}{u}}\right)^{n}{% endequation %} ולכן כדאי לנו למצוא חסם כלשהו על מה שבפנים, {% equation %}\frac{1}{1-\frac{n}{u}}{% endequation %}. לצורך כך כדאי להיזכר שהדבר הזה נראה כמו סכום של טור גיאומטרי. באופן כללי, אם {% equation %}\left|q\right|&lt;1{% endequation %}, אז מתקיים

{% equation %}\sum_{k=0}^{\infty}q^{k}=\frac{1}{1-q}{% endequation %}

ובמקרה שלנו {% equation %}u&gt;2n{% endequation %} (ממש ממש גדול יותר, אם תציצו שניה במה שדרשנו עליו) כך ש-{% equation %}\frac{n}{u}&lt;\frac{1}{2}{% endequation %}, ולכן:

{% equation %}\frac{1}{1-\frac{n}{u}}=\sum_{k=0}^{\infty}\left(\frac{n}{u}\right)^{k}=1+\left(\frac{n}{u}\right)\sum_{k=0}^{\infty}\left(\frac{n}{u}\right)^{k}&lt;1+\frac{n}{u}\sum_{k=0}^{\infty}\left(\frac{1}{2}\right)^{k}=1+\frac{2n}{u}{% endequation %}

כל המעברים כאן הם חשבון פשוט, אבל את השני ביצעתי קצת בזריזות: פשוט הוצאתי מהסכום את האיבר הראשון שלו (1) ואז הוצאתי החוצה גורם משותף לשאר האיברים ({% equation %}\frac{n}{u}{% endequation %}).

עכשיו, מה קורה כשמעלים את זה בחזקת {% equation %}n{% endequation %}? אפשר להשתמש בבינום של ניוטון ולקבל:

{% equation %}\left(1+\frac{2n}{u}\right)^{n}=\sum_{k=0}^{n}{n \choose k}\left(\frac{2n}{u}\right)^{k}&lt;1+\frac{2n}{u}\sum_{k=1}^{n}{n \choose k}&lt;1+\frac{2n}{u}2^{n}{% endequation %}

גם פה רוב המעברים הם פשוטים - הראשון הוא הבינום, השני הוא פשוט פירוק לאיבר ראשון בסכום וכל היתר והוצאת גורם משותף והתעלמות מהיתר, בהתבסס על כך ש-{% equation %}\frac{2n}{u}&lt;1{% endequation %}, והמעבר השלישי הוא פשוט הנוסחה {% equation %}\sum_{k=0}^{n}{n \choose k}=2^{n}{% endequation %} בפעולה.

בואו נזכר ממה התחלנו: {% equation %}u^{n}/{u \choose n}{% endequation %}. הגענו לכך שהוא קטן מ-{% equation %}n!\frac{1}{\left(1-\frac{n}{u}\right)^{n}}{% endequation %}, ולכן:

{% equation %}u^{n}/{u \choose n}&lt;n!+\frac{2n}{u}2^{n}n!&lt;n!+\frac{2^{n+1}n^{n+1}}{u}&lt;n!+1{% endequation %}

המעבר הלפני אחרון נובע מכך ש-{% equation %}n!&lt;n^{n}{% endequation %} (כמובן - בשני המקרים מכפילים {% equation %}n{% endequation %} איברים אבל ב-{% equation %}n!{% endequation %} רובם קטנים יותר מ-{% equation %}n{% endequation %}) המעבר האחרון נובע מההנחה שלנו על {% equation %}u{% endequation %}: {% equation %}u&gt;\left(2n\right)^{n+1}{% endequation %}. זה מסיים את ההוכחה כי זה מראה ש-{% equation %}n!\le u^{n}/{u \choose n}&lt;n!+1{% endequation %} ולכן לקיחת ערך שלם תמיד תחזיר לנו {% equation %}n!{% endequation %}. אם עוד לא ברור למה הביטוי הזה הוא לפחות {% equation %}n!{% endequation %}, זכרו ש-{% equation %}u^{n}/{u \choose n}=\frac{u^{n}}{u\left(u-1\right)\left(u-2\right)\cdots\left(u-n+1\right)}n!{% endequation %} - במונה ובמכנה יש {% equation %}n{% endequation %} מוכפלים, אבל במונה כולם {% equation %}u{% endequation %} ובמכנה רובם קטנים מ-{% equation %}u{% endequation %}.

עכשיו אפשר להוכיח ש-{% equation %}n!{% endequation %} דיופנטית בהתבסס על כך ש-{% equation %}{n \choose k}{% endequation %} דיופנטית. הביטוי הדיופנטי הוא פשוט למדי:

{% equation %}m=n!\iff\exists u\left[{u \choose n}m\le u^{n}\wedge u^{n}\le{u \choose n}\left(m+1\right)\wedge u&gt;\left(2n\right)^{n+1}\right]{% endequation %}

יפה. הראינו כבר על שלוש פונקציות שגדלות "מהר" שהן דיופנטיות - {% equation %}n^{k},{n \choose k},n!{% endequation %}. עכשיו אפשר לעבור לפונקציה שהיא היעד הסופי שלנו, ובהשוואה לשלוש הפונקציות הטבעיות הללו אולי תהיה טיפה מאכזבת: {% equation %}h\left(a,b,y\right)=\prod_{k=1}^{y}\left(a+bk\right){% endequation %}. מילולית, הפונקציה כופלת את {% equation %}y{% endequation %} האיברים הראשונים בסדרה חשבונית שהאיבר הראשון שלה הוא {% equation %}a+b{% endequation %} וההפרש בין שני איברים סמוכים הוא {% equation %}b{% endequation %}. למה הפונקציה הזו דווקא כל כך יעילה? ובכן... אה... זה טכני, חכו ותראו. לא תהיה תובנה מדהימה בסוף.

כדי להראות שהפונקציה הזו דיופנטית נשתמש בתעלול שאיכשהו יערבב את כל שלוש הפונקציות שראינו עד כה. ראשית, נניח שיש לנו {% equation %}q,M{% endequation %} שעבורם מתקיימת המשוואה {% equation %}bq\equiv_{M}a{% endequation %}. אז נרצה להראות שהקסם הבא מתקיים:

{% equation %}\prod_{k=1}^{y}\left(a+bk\right)\equiv_{M}b^{y}y!{q+y \choose y}{% endequation %}

ההוכחה דווקא פשוטה למדי הפעם. פשוט נפתח את הביטוי:

{% equation %}b^{y}y!{q+y \choose y}=b^{y}y!\frac{\left(q+y\right)!}{y!q!}=b^{y}\left(q+y\right)\left(q+y-1\right)\cdots\left(q+1\right){% endequation %}

{% equation %}=\left(bq+by\right)\left(bq+b\left(y-1\right)\right)\cdots\left(bq+b\right)\equiv_{M}\prod_{k=1}^{y}\left(a+bk\right){% endequation %}

מה שנותר לעשות הוא להבטיח שאכן קיימים {% equation %}M,q{% endequation %} שמקיימים את המשוואה {% equation %}bq\equiv_{M}a{% endequation %}. בגלל האותיות העסק יכול להיראות מבלבל, אז בואו נשכח לרגע מהכל ונעבור לדון במשהו כללי - המשוואה הלינארית {% equation %}ax\equiv_{n}b{% endequation %} כאשר {% equation %}a,b,n{% endequation %} נתונים ואילו {% equation %}x{% endequation %} הוא המשתנה. הטענה היא שלמשוואה הזו קיים פתרון אם {% equation %}\left(a,n\right)=1{% endequation %}, כלומר {% equation %}a{% endequation %} זר ל-{% equation %}n{% endequation %}. הסיבה לכך היא שבמקרה הזה, קיים ל-{% equation %}a{% endequation %} הופכי כפלי מודולו {% equation %}n{% endequation %} ולכן {% equation %}x\equiv_{n}a^{-1}b{% endequation %}. במקרה שלנו ה"משתנה" הוא בכלל {% equation %}q{% endequation %} ומה שאנחנו צריכים כדי שהמשוואה תהיה פתירה הוא שיתקיים {% equation %}\left(b,M\right)=1{% endequation %}; למזלנו, אנחנו יכולים לבחור את {% equation %}M{% endequation %} כדי להבטיח שזה יקרה: נבחר {% equation %}M=b\left(a+by\right)^{y}+1{% endequation %}, אז אגף ימין בודאות לא מתחלק על ידי אף ראשוני שמחלק את {% equation %}b{% endequation %} (כי כפלנו את {% equation %}b{% endequation %} במשהו והוספנו 1) ולכן {% equation %}\left(M,b\right){% endequation %} זרים ומובטח לנו שקיים {% equation %}q{% endequation %} כלשהו (לא יודע מי) כך ש-{% equation %}bq\equiv_{M}a{% endequation %}. את כל זה אפשר לכתוב בתור ביטוי דיופנטי:

{% equation %}z=\prod_{k=1}^{y}\left(a+bk\right)\iff\exists M,q,t,p{% endequation %}

{% equation %}M=b\left(a+by\right)^{y}+1\wedge bq=a+Mt{% endequation %}

{% equation %}\wedge z&lt;M\wedge z+Mp=b^{y}y!{q+y \choose y}{% endequation %}

ובזאת סיימנו את שלב בניית הכלים. סוף סוף יש לנו את מה שמאפשר להוכיח שהכמת האוניברסלי החסום הוא דיופנטי - הצעד האחרון בהוכחה כולה!

בואו נעבור על מה שאנחנו רוצים לעשות. ביטוי דיופנטי מתורגם בסופו של דבר לפולינום {% equation %}P{% endequation %} ולמשוואה

{% equation %}\exists y_{1},\dots,y_{m}\left[P\left(x_{1},\dots,x_{n},y_{1},\dots,y_{m}\right)=0\right]{% endequation %}

שמגדירה קבוצה - בדיוק את קבוצת ה-{% equation %}x{% endequation %}-ים שכשמציבים אותם מקבלים משוואה פתירה.

מה שאנחנו רוצים לעשות הוא להוכיח שגם את הביטוי הבא:

{% equation %}\forall z\le y\exists y_{1},\dots,y_{m}\left[P\left(x_{1},\dots,x_{n},z,y,y_{1},\dots,y_{m}\right)=0\right]{% endequation %}

עבור פולינום {% equation %}P{% endequation %} כלשהו, אפשר להמיר לביטוי מהסוג שלעיל, שלא כולל כמת "לכל" ועדיין מגדיר את אותה קבוצת {% equation %}x{% endequation %}-ים שכשמציבים אותם מקבלים משוואה פתירה. אבחנה אחת להתחלה היא שהביטוי שכתבתי כרגע שקול לביטוי

{% equation %}\exists u\forall_{\le y}z\exists_{\le u}y_{1},\dots,y_{m}\left[P\left(x_{1},\dots,x_{n},z,y,y_{1},\dots,y_{m}\right)=0\right]{% endequation %}

שבו אני מגביל את {% equation %}z{% endequation %} להיות קטן או שווה ל-{% equation %}y{% endequation %} כלשהו ומגביל את כל ה-{% equation %}y_{i}{% endequation %}-ים להיות קטנים מ-{% equation %}u{% endequation %} כלשהו שכמובן קיים בהנחה שקיימים {% equation %}y_{i}{% endequation %}-ים שפותרים את המשוואה (פשוט קחו את המקסימום מביניהם).

עכשיו לאקשן. אני טוען שבהינתן פולינום {% equation %}Q{% endequation %} מתאים, הביטוי הבא:

{% equation %}\forall_{\le y}z\exists_{\le u}y_{1},\dots,y_{m}\left[P\left(x_{1},\dots,x_{n},z,y,y_{1},\dots,y_{m}\right)=0\right]{% endequation %}

שקול לביטוי המפלצתי הבא, שהחשיבות שלו בכך שהוא <strong>לא כולל</strong> את הכמת האוניברסלי:

{% equation %}\exists c,t,a_{1},\dots,a_{m}{% endequation %}

{% equation %}1+ct=\prod_{k=1}^{y}1+kt{% endequation %}

{% equation %}\wedge t=Q\left(y,u,x_{1},\dots,x_{n}\right)!\wedge1+ct|\prod_{j=1}^{u}\left(a_{1}-j\right){% endequation %}

{% equation %}\wedge\dots\wedge1+ct|\prod_{j=1}^{u}\left(a_{m}-j\right){% endequation %}

{% equation %}\wedge P\left(x_{1},\dots,x_{n},c,y,a_{1},\dots,a_{m}\right)\equiv_{1+ct}0{% endequation %}

כדי שזה יעבוד, {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right){% endequation %} צריך לקיים את שלוש התכונות הבאות:

{% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)&gt;u{% endequation %}

{% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)&gt;y{% endequation %}

אם {% equation %}z\le y{% endequation %} וגם {% equation %}y_{1},\dots,y_{m}\le u{% endequation %} אז

{% equation %}\left|P\left(x_{1},\dots,x_{n},z,y,y_{1},\dots,y_{m}\right)\right|\le Q\left(y,u,x_{1},\dots,x_{n}\right){% endequation %}

זהו. אם נצליח לעשות את זה, גמרנו, שכן בבירור הביטוי המפלצתי שכתבתי הוא דיופנטי - הוא כולל רק את {% equation %}\prod\left(a+bk\right){% endequation %} שכבר ראינו שהיא דיופנטית, ואת היחס {% equation %}a|b{% endequation %} ("{% equation %}a{% endequation %} מחלק את {% equation %}b{% endequation %}") שכבר ראינו שהוא דיופנטי, ואת היחס {% equation %}\equiv{% endequation %} שכבר ראינו שהוא דיופנטי, ואת הפונקציה {% equation %}n!{% endequation %} שכבר ראינו שהיא דיופנטית.

עכשיו מכיוון שזו הוכחת שקילות, צריך להוכיח שני כיוונים. בואו נניח קודם כל שיש לנו {% equation %}x_{1},\dots,x_{n},y,u{% endequation %} שעבורם הביטוי הדיופנטי המפלצתי הוא נכון (כלומר, יש פתרון למשוואות שלו) ונראה שקיים ערך של {% equation %}z{% endequation %} שחסום על ידי {% equation %}y{% endequation %} כך שעבורו קיימים ערכים של {% equation %}y_{i}{% endequation %}-ים שחסומים על ידי {% equation %}u{% endequation %} כך ש-{% equation %}P\left(x_{1},\dots,x_{n},z,y,y_{1},\dots,y_{m}\right)=0{% endequation %}.

בואו נניח ש-{% equation %}z=k{% endequation %}, כאשר {% equation %}1\le k\le y{% endequation %}. אנחנו רוצים למצוא {% equation %}y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}{% endequation %} כך ש-{% equation %}P\left(x_{1},\dots,x_{n},y,k,y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}\right)=0{% endequation %}. אנחנו יודעים שהביטוי הדיופנטי המפלצתי פתיר. אז בואו ניקח את הצבת הערכים לתוכו ונשתמש בה. בפרט, הצבת הערכים הזו נותנת לנו {% equation %}a_{1},\dots,a_{m}{% endequation %} ו-{% equation %}t{% endequation %}. בואו נסמן ב-{% equation %}p_{k}{% endequation %} גורם ראשוני כלשהו של {% equation %}1+kt{% endequation %}, וכעת נגדיר:

{% equation %}y_{i}^{\left(k\right)}=a_{i}\mbox{ mod }p_{k}{% endequation %}

דהיינו, {% equation %}y_{i}^{\left(k\right)}{% endequation %} מתקבל מחלוקת {% equation %}a_{i}{% endequation %} ב-{% equation %}p_{k}{% endequation %} ולקיחת השארית. אני טוען שהערכים הללו אכן מספקים את {% equation %}P{% endequation %}, ושהם לא גדולים מ-{% equation %}u{% endequation %}, כלומר {% equation %}1\le y_{i}^{\left(k\right)}\le u{% endequation %}. מדוע?

ובכן, ראשית נטפל בעניין הגודל. שימו לב לכך ש-{% equation %}p_{k}|1+kt{% endequation %} (כי בחרנו את {% equation %}p_{k}{% endequation %} להיות גורם של הביטוי הימני), וש-{% equation %}1+kt|1+ct{% endequation %} (זה נובע מייד מהמשוואה הראשונה בביטוי המפלצתי) וש-{% equation %}1+ct|\prod_{j=1}^{u}\left(a_{i}-j\right){% endequation %} (זו אחת מהמשוואות בביטוי המפלצתי). מסקנה: {% equation %}p_{k}|\prod_{j=1}^{u}\left(a_{i}-j\right){% endequation %}, אבל מכיוון שלקחנו את {% equation %}p_{k}{% endequation %} להיות ראשוני, אם הוא מחלק מכפלה הוא מחלק אחד מאיבריה, כלומר יש {% equation %}j{% endequation %} ספציפי כלשהו כך ש-{% equation %}p_{k}|a_{i}-j{% endequation %}. מסקנה: {% equation %}a_{i}\equiv_{p_{k}}j\equiv_{p_{k}}y_{i}^{\left(k\right)}{% endequation %}.

אם אצליח לשכנע אתכם ש-{% equation %}y_{i}^{\left(k\right)}=j{% endequation %} זה יראה ש-{% equation %}y_{i}^{\left(k\right)}{% endequation %} קטן מספיק, כי {% equation %}1\le j\le u{% endequation %}. כעת, {% equation %}y_{i}^{\left(k\right)}{% endequation %} התקבל מחלוקה של משהו ב-{% equation %}p_{k}{% endequation %} ולקיחת השארית, כלומר הוא אוטומטית קטן מ-{% equation %}p_{k}{% endequation %}. אם נוכיח ש-{% equation %}j&lt;p_{k}{% endequation %} זה יסיים את העניין כי שני מספרים ששקולים מודולו {% equation %}p_{k}{% endequation %} ושניהם קטנים מ-{% equation %}p_{k}{% endequation %} חייבים להיות שווים. כדי להראות ש-{% equation %}j&lt;p_{k}{% endequation %} מספיק להראות ש-{% equation %}u&lt;p_{k}{% endequation %}. כעת נכניס את {% equation %}Q{% endequation %} לתמונה: כזכור, {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)&gt;u{% endequation %}, ולכן די לנו להראות ש-{% equation %}p_{k}&gt;Q\left(y,u,x_{1},\dots,x_{n}\right){% endequation %}. איך נעשה את זה? ובכן, בואו נסתכל על הביטוי המפלצתי ונראה איך {% equation %}Q{% endequation %} בא לידי ביטוי בו.

יש רק משוואה אחת שמערבת את {% equation %}Q{% endequation %}: {% equation %}t=Q\left(y,u,x_{1},\dots,x_{n}\right)!{% endequation %}. מילולית זה אומר ש-{% equation %}t{% endequation %} הוא מכפלת <strong>כל</strong> המספרים הטבעיים עד וכולל {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right){% endequation %}. כעת, אם מישהו מחלק את {% equation %}1+kt{% endequation %} אז הוא לא מחלק את {% equation %}t{% endequation %}, ולכן הוא לא יכול להיות אף אחד מהמספרים הטבעיים עד וכולל {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right){% endequation %}. מסקנה: {% equation %}p_{k}&gt;Q\left(y,u,x_{1},\dots,x_{n}\right)!{% endequation %}, וזה מה שרצינו.

הראינו אם כן שה-{% equation %}y_{i}^{\left(k\right)}{% endequation %}-ים הם בסדר הגודל הנכון, אבל למה הם פותרים את {% equation %}P{% endequation %}?

ובכן, מכיוון ש-{% equation %}p_{k}{% endequation %} מחלק את {% equation %}1+kt{% endequation %} וגם את {% equation %}1+ct{% endequation %} הרי שקיבלנו:

{% equation %}1+ct\equiv_{p_{k}}0{% endequation %}

{% equation %}1+kt\equiv_{p_{k}}0{% endequation %}

נכפול את המשוואה הראשונה ב-{% equation %}k{% endequation %}, את השניה ב-{% equation %}c{% endequation %}, ונקבל:

{% equation %}k+kct\equiv_{p_{k}}0{% endequation %}

{% equation %}c+kct\equiv_{p_{k}}0{% endequation %}

נשווה את שתיהן ונקבל ש-{% equation %}k\equiv_{p_{k}}c{% endequation %}. כמו כן, אנחנו זוכרים שעל פי הגדרתם, {% equation %}y_{i}^{\left(k\right)}\equiv_{p_{k}}a_{i}{% endequation %}. המסקנה:

{% equation %}P\left(x_{1},\dots,x_{n},k,y,y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}\right)\equiv_{p_{k}}P\left(x_{1},\dots,x_{n},c,y,a_{1},\dots,a_{m}\right)\equiv_{p_{k}}0{% endequation %}

(המעבר השני נובע מכך ש-{% equation %}P\equiv_{1+ct}0{% endequation %} ו-{% equation %}p_{k}{% endequation %} מחלק את {% equation %}1+ct{% endequation %}).

עכשיו, השוויון שלעיל לא אומר ש-{% equation %}P\left(x_{1},\dots,x_{n},k,y,y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}\right)=0{% endequation %}, רק שקול לאפס מודולו {% equation %}p_{k}{% endequation %}. כדי להראות שוויון לאפס צריך להראות שהביטוי הזה גם קטן מ-{% equation %}p_{k}{% endequation %}. אבל זה שוב נובע מ-{% equation %}Q{% endequation %}, הפעם מהתכונה השלישית שלו:

{% equation %}\left|P\left(x_{1},\dots,x_{n},k,y,y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}\right)\right|\le Q\left(y,u,x_{1},\dots,x_{n}\right)&lt;p_{k}{% endequation %}

וסיימנו את כיוון הגרירה הראשון, לפיו אם {% equation %}x_{1},\dots,x_{n}{% endequation %} פותרים את הביטוי המפלצתי הם פותרים את {% equation %}P{% endequation %} ה"רגיל".

נותר הכיוון השני. נניח שעבור {% equation %}x_{1},\dots,x_{n},y{% endequation %}, לכל {% equation %}1\le k\le y{% endequation %} יש {% equation %}y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}{% endequation %} כך ש-

{% equation %}P\left(x_{1},\dots,x_{n},k,y,y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}\right)=0{% endequation %}.

אנחנו רוצים עכשיו להוכיח קיום של {% equation %}t,c,a_{1},\dots,a_{m}{% endequation %} שפותרים את מערכת המשוואות המפלצתית.

נסמן בתור {% equation %}u{% endequation %} מספר שגדול מכל ה-{% equation %}y_{i}^{\left(k\right)}{% endequation %}-ים הללו. כעת, נגדיר {% equation %}t=Q\left(y,u,x_{1},\dots,x_{n}\right)!{% endequation %}. נותר לנו להגדיר את {% equation %}c{% endequation %} ואת ה-{% equation %}a_{i}{% endequation %}-ים.

כעת, {% equation %}1+kt\equiv_{t}1{% endequation %} ולכן {% equation %}\prod_{k=1}^{y}\left(1+kt\right)\equiv_{t}1{% endequation %}. המשמעות הישירה של השקילות הזו היא שקיים {% equation %}c{% endequation %} כך ש-{% equation %}\prod_{k=1}^{y}\left(1+kt\right)=1+ct{% endequation %}, כך שמצאנו את ה-{% equation %}c{% endequation %} שלנו והוא מקיים את המשוואה הראשונה בביטוי המפלצתי. נשאר רק לבחור את ה-{% equation %}a_{i}{% endequation %}-ים כך שיקיימו את המשוואות {% equation %}1+ct|\prod_{j=1}^{u}\left(a_{i}-j\right){% endequation %}, וכך שיתקיים {% equation %}P\left(x_{1},\dots,x_{n},c,y,a_{1},\dots,a_{m}\right)\equiv_{1+ct}0{% endequation %}. זה השלב שידרוש תחכום ושימוש במשפט השאריות הסיני.

מה שאני רוצה לעשות הוא להגדיר את {% equation %}a_{i}{% endequation %} להיות הפתרון למערכת המשוואות {% equation %}a_{i}\equiv_{1+kt}y_{i}^{\left(k\right)}{% endequation %}, {% equation %}1\le k\le y{% endequation %} (זה לא כל כך מפתיע מבחינה רעיונית - אם אתם עוד מצליחים לעקוב אחרי מה שקורה בהוכחה ברמת התמונה הגדולה - אני בקושי מצליח - אפשר לראות שה-{% equation %}a_{i}{% endequation %}-ים הללו אמורים לקודד בתוכם איכשהו את הפתרונות ל-{% equation %}P{% endequation %} עבור כל בחירה של {% equation %}k{% endequation %} בתחום המתאים). כדי להראות שקיים פתרון למערכת הזו צריך להוכיח שכל המודולוסים זרים, כלומר ש-{% equation %}\left(1+kt,1+lt\right)=1{% endequation %} עבור {% equation %}1\le l&lt;k\le y{% endequation %}. נניח בשלילה שיש איזה ראשוני {% equation %}p{% endequation %} שמחלק את שניהם, אז הוא מחלק גם את ההפרש שלהם, כלומר {% equation %}p|t\left(k-l\right){% endequation %}. שימו לב ש-{% equation %}p{% endequation %} לא יכול לחלק את {% equation %}t{% endequation %}, אחרת הוא לא היה מחלק את {% equation %}1+kt{% endequation %}, ולכן בהכרח {% equation %}p|k-l{% endequation %}. בפרט זה אומר ש-{% equation %}p&lt;y{% endequation %}. כעת, תעלול! הגדרנו {% equation %}t=Q\left(y,u,x_{1},\dots,x_{n}\right)!{% endequation %}, והרי {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)&gt;y{% endequation %}, ולכן כל מספר עד {% equation %}y{% endequation %} נכלל במכפלה שמרכיבה את {% equation %}t{% endequation %}, ולכן {% equation %}p{% endequation %} חייב לחלק את {% equation %}t{% endequation %} וזו סתירה. מסקנה: {% equation %}\left(1+kt,1+lt\right)=1{% endequation %} ואפשר להשתמש במשפט השאריות הסיני כפי שרצינו כדי למצוא את ה-{% equation %}a_{i}{% endequation %}-ים.

למה זה עזר לנו? ובכן, שימו לב כי לכל {% equation %}k{% endequation %} אנחנו מקבלים:

{% equation %}P\left(x_{1},\dots,x_{n},c,y,a_{1},\dots,a_{m}\right)\equiv_{1+kt}P\left(x_{1},\dots,x_{n},k,y,y_{1}^{\left(k\right)},\dots,y_{m}^{\left(k\right)}\right)=0{% endequation %}

כלומר, לכל {% equation %}1\le k\le y{% endequation %} קיבלנו ש-{% equation %}1+kt{% endequation %} מחלק את {% equation %}P\left(x_{1},\dots,x_{n},c,y,a_{1},\dots,a_{m}\right){% endequation %}. מכיוון שכל ה-{% equation %}1+kt{% endequation %}-ים זרים זה לזה, אפשר להשתמש במשפט נוסף: אם שני מספרים זרים זה לזה מחלקים את אותו מספר, גם המכפלה שלהם מחלקת אותו. בסימנים: אם {% equation %}a|c{% endequation %} וגם {% equation %}b|c{% endequation %} וגם {% equation %}\left(a,b\right)=1{% endequation %} אז {% equation %}ab|c{% endequation %}.

המסקנה שלנו היא ש-{% equation %}1+ct=\prod_{k=1}^{y}1+kt{% endequation %} מחלק את {% equation %}P\left(x_{1},\dots,x_{n},c,y,a_{1},\dots,a_{m}\right){% endequation %}, וזו בדיוק המשוואה האחרונה בביטוי המפלצתי. כמעט סיימנו. נשאר רק להראות שמתקיים {% equation %}1+ct|\prod_{j=1}^{u}\left(a_{i}-j\right){% endequation %} לכל {% equation %}a_{i}{% endequation %}. לשם כך מספיק, כפי שראינו, להראות שלכל {% equation %}a_{i}{% endequation %} ולכל {% equation %}k{% endequation %} מתקיים {% equation %}1+kt|\prod_{j=1}^{u}\left(a_{i}-j\right){% endequation %}. כדי לחלק מכפלה מספיק לחלק איבר אחד שלה, כלומר מספיק לנו להראות שלכל {% equation %}a_{i}{% endequation %} ולכל {% equation %}k{% endequation %} קיים {% equation %}j{% endequation %} כך ש-{% equation %}1+kt|a_{i}-j{% endequation %}, אבל זה קל: מכיוון שהגדרנו את {% equation %}a_{i}{% endequation %} להיות איבר שמקיים {% equation %}a_{i}\equiv_{1+kt}y_{i}^{\left(k\right)}{% endequation %} זה אומר ש-{% equation %}1+kt{% endequation %} מחלק את {% equation %}a_{i}-y_{i}^{\left(k\right)}{% endequation %} ולכן {% equation %}y_{i}^{\left(k\right)}{% endequation %} הוא ה-{% equation %}j{% endequation %} שלנו; רק צריך לשים לב לכך ש-{% equation %}1\le y_{i}^{\left(k\right)}\le u{% endequation %} ולכן הוא בתחום המתאים (הנה לנו הסיבה שבגללה היה חשוב להגביל את הערכים של ה-{% equation %}y_{i}{% endequation %}-ים).

סיימנו!

...

או שלא. מה עוד חסר? הפולינום {% equation %}Q{% endequation %}. הרי אמרתי "אני טוען שבהינתן פולינום {% equation %}Q{% endequation %} מתאים..." ואחר כך נתתי שלוש דרישות ש-{% equation %}Q{% endequation %} צריך לקיים. אני עדיין צריך להציג את {% equation %}Q{% endequation %} הזה, ובכך נסיים סופית את ההוכחה.

הבניה של {% equation %}Q{% endequation %} אינה מורכבת, אבל כיף זה לא הולך להיות. בואו פשוט נראה אותה. ראשית כל, בואו נציג את {% equation %}P{% endequation %} בתור סכום של מונומים, כלומר נכתוב

{% equation %}P\left(x_{1},\dots,x_{n},k,y,y_{1},\dots,y_{m}\right)=\sum_{r=1}^{N}t_{r}{% endequation %}

כך שכל מונום הוא בעל המראה המזעזע הבא:

{% equation %}t_{r}=cx_{1}^{q_{1}}\cdots x_{n}^{q_{n}}k^{a}y^{b}y_{1}^{s_{1}}\cdots y_{m}^{s_{m}}{% endequation %}

בואו נגדיר מונום חדש, {% equation %}u_{r}{% endequation %}, על בסיס {% equation %}t_{r}{% endequation %}:

{% equation %}u_{r}=\left|c\right|y^{a+b}x_{1}^{q_{1}}\cdots x_{n}^{q_{n}}u^{s_{1}+\dots s_{m}}{% endequation %}

ועכשיו נגדיר את {% equation %}Q{% endequation %}:

{% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)=u+y+\sum_{r=1}^{N}u_{r}{% endequation %}

בבירור מתקיים {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)&gt;u{% endequation %} וגם {% equation %}Q\left(y,u,x_{1},\dots,x_{n}\right)&gt;y{% endequation %} רק מעצם הבניה (זכרו שכל הערכים שאפשר להציב בפולינום הם חיוביים). צריך רק להסביר למה מתקיים

{% equation %}\left|P\left(x_{1},\dots,x_{n},k,y,y_{1},\dots,y_{m}\right)\right|\le Q\left(y,u,x_{1},\dots,x_{n}\right){% endequation %}

וזאת, כזכור, בתנאי ש-{% equation %}k\le y{% endequation %} וגם {% equation %}y_{1},\dots,y_{m}\le u{% endequation %}.

אז למה זה נכון? ובכן, עם אי-שוויון המשולש נקבל:

{% equation %}\left|P\left(x_{1},\dots,x_{n},k,y,y_{1},\dots,y_{m}\right)\right|\le\sum_{r=1}^{N}\left|t_{r}\right|{% endequation %}

לכן מספיק להשוות מונום-מונום ולהראות ש-{% equation %}\left|t_{r}\right|\le u_{r}{% endequation %}.

את {% equation %}t_{r}{% endequation %} אפשר להפריד לשלושה חלקים. הראשון הוא {% equation %}\left|c\right|x_{1}^{q_{1}}\cdots x_{n}^{q_{n}}{% endequation %} שקיים כמו שהוא גם ב-{% equation %}u_{r}{% endequation %}; השני הוא {% equation %}k^{a}y^{b}{% endequation %} שמכוסה על ידי {% equation %}y^{a+b}{% endequation %} של {% equation %}u_{r}{% endequation %} בתנאי ש-{% equation %}k\le y{% endequation %}; והשלישי הוא {% equation %}y_{1}^{s_{1}}\cdots y_{m}^{s_{m}}{% endequation %} שמכוסה על ידי {% equation %}u^{s_{1}+\dots s_{m}}{% endequation %} בתנאי ש-{% equation %}y_{i}\le u{% endequation %}. זה מסיים את הבניה של {% equation %}Q{% endequation %}, ולכן מסיים את ההוכחה של הטענה לפיה אפשר לבנות ביטויים דיופנטיים עם הכמת האוניברסלי החסום, ולכן מסיים את ההוכחה שהבעיה העשירית של הילברט לא כריעה!

לא ברור לי כמה מכם הצליחו לשרוד איתי עד לשלב הזה; אכתוב עוד פוסט סיכום (קצר) כדי לחזור על מה שהלך פה ממעוף הציפור ולסיים עם בונוס קטן שקשור למספרים הראשוניים.
